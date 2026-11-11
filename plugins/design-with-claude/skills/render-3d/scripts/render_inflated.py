"""Step 2 of the inflated 3D title: turn the height maps from inflate_text.py into 3D meshes and render
them with Blender Cycles (front material on top of a glossy rim/base shell), transparent background.

Usage:  python3.11 render_inflated.py config.json [preview]
        'preview' renders small and fast (about 20 s) for checking shapes; omit it for the final render.
Writes: <out_dir>/title.png (RGBA, transparent) -> place it in the piece with the PSD builder.

Requirements: Python 3.11 + pip install bpy numpy (bpy is Blender as a Python module, ~300 MB, CPU only).
Config keys used here (see ../examples/spooky_class.json):
  front {"color": [r,g,b] 0-1, "roughness", "metallic", "coat", "subsurface"}
  rim   {"color", "roughness", "metallic", "coat"}   (ignored if the pieces have no rim)
  world {"color", "strength"}                          (tints reflections; keep it dark and on-palette)
  lights: "studio" (default)  key strip top-left, warm fill right, low bounce, soft top
  height  height exaggeration (0.55 default; higher = puffier)
  render {"scale": 0.75, "samples": 40, "step": 2}
"""
import json, sys
import numpy as np
import bpy
from mathutils import Vector

cfg = json.load(open(sys.argv[1]))
PREVIEW = len(sys.argv) > 2 and sys.argv[2] == "preview"
OUT = cfg["out_dir"].rstrip("/") + "/"
PX, HK = 0.01, float(cfg.get("height", 0.55))
R = cfg.get("render", {})
SCALE, SAMPLES, STEP = (0.35, 16, 4) if PREVIEW else (R.get("scale", 0.75), R.get("samples", 40), R.get("step", 2))

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = SAMPLES; sc.cycles.use_denoising = True
sc.render.film_transparent = True
sc.view_settings.view_transform = "Standard"; sc.view_settings.look = "Medium High Contrast"


def build(name, h, z0):
    h = h[::STEP, ::STEP]
    rows, cols = h.shape
    xs = (np.arange(cols) * STEP - cols * STEP / 2) * PX
    ys = -(np.arange(rows) * STEP - rows * STEP / 2) * PX
    inside = h > 0
    use = np.zeros_like(inside)
    c = inside[:-1, :-1]
    use[:-1, :-1] |= c; use[1:, :-1] |= c; use[:-1, 1:] |= c; use[1:, 1:] |= c
    idx = -np.ones(h.shape, np.int64)
    vy, vx = np.nonzero(use); idx[vy, vx] = np.arange(len(vy))
    verts = np.stack([xs[vx], ys[vy], z0 + h[vy, vx] * PX * HK], 1)
    cy, cx = np.nonzero(c)
    faces = np.stack([idx[cy, cx], idx[cy, cx + 1], idx[cy + 1, cx + 1], idx[cy + 1, cx]], 1)
    me = bpy.data.meshes.new(name)
    me.vertices.add(len(verts)); me.vertices.foreach_set("co", verts.astype(np.float32).ravel())
    me.loops.add(faces.size); me.loops.foreach_set("vertex_index", faces.astype(np.int32).ravel())
    me.polygons.add(len(faces))
    me.polygons.foreach_set("loop_start", (np.arange(len(faces)) * 4).astype(np.int32))
    me.polygons.foreach_set("loop_total", np.full(len(faces), 4, np.int32))
    me.update(); me.validate(); me.shade_smooth()
    o = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(o)
    return o


def material(name, p):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*p["color"], 1)
    b.inputs["Roughness"].default_value = p.get("roughness", 0.3)
    b.inputs["Metallic"].default_value = p.get("metallic", 0.0)
    b.inputs["Coat Weight"].default_value = p.get("coat", 0.4)
    b.inputs["Coat Roughness"].default_value = 0.04
    b.inputs["Subsurface Weight"].default_value = p.get("subsurface", 0.0)
    b.inputs["Subsurface Radius"].default_value = (0.3, 0.2, 0.15)
    return m


P = np.load(OUT + "pieces.npz")
Hh, Ww = (int(v) for v in P["shape"]); n = int(P["n"][0])
FRONT = material("Front", cfg.get("front", {"color": [0.84, 0.75, 0.63], "roughness": 0.32, "coat": 0.4, "subsurface": 0.15}))
RIMM = material("Rim", cfg.get("rim_material", {"color": [0.38, 0.0, 0.015], "roughness": 0.12, "metallic": 0.35, "coat": 1.0}))
for i in range(n):                       # later letters sit slightly higher -> their rim overlaps the previous one
    y0, x0 = P[f"o{i}"]; z = i * 0.08
    for key, zz, mat in ((f"r{i}", z, RIMM), (f"c{i}", z + 0.14, FRONT)):
        if key not in P.files:
            continue
        full = np.zeros((Hh, Ww), np.float32); a = P[key]
        full[y0:y0 + a.shape[0], x0:x0 + a.shape[1]] = a
        build(key, full, zz).data.materials.append(mat)

wcfg = cfg.get("world", {"color": [0.3, 0.06, 0.07], "strength": 0.45})
world = bpy.data.worlds.new("w"); sc.world = world; world.use_nodes = True
bg = world.node_tree.nodes["Background"]
bg.inputs["Color"].default_value = (*wcfg["color"], 1); bg.inputs["Strength"].default_value = wcfg["strength"]


def area(loc, size, power, color, sy=None):
    l = bpy.data.lights.new("a", "AREA"); l.energy = power; l.color = color
    l.shape = "RECTANGLE"; l.size = size; l.size_y = sy or size
    o = bpy.data.objects.new("a", l); o.location = loc; bpy.context.collection.objects.link(o)
    o.rotation_euler = (Vector((0, 0, 0)) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()


area((-9, 9, 12), 7, 2300, (1, 0.97, 0.94), 2.5)   # key strip, top-left: white glints on upper-left edges
area((10, 4, 9), 5, 600, (1, 0.85, 0.75))          # warm fill, right
area((0, -12, 6), 10, 350, (1, 0.3, 0.3), 2)       # low bounce
area((0, 0, 20), 14, 300, (1, 0.9, 0.85))          # soft top

cd = bpy.data.cameras.new("cam"); cd.type = "ORTHO"; cd.ortho_scale = Ww * PX
cam = bpy.data.objects.new("cam", cd); bpy.context.collection.objects.link(cam)
cam.location = (0, 0, 40); sc.camera = cam
sc.render.resolution_x = int(Ww * SCALE); sc.render.resolution_y = int(Hh * SCALE)
sc.render.filepath = OUT + ("title_preview.png" if PREVIEW else "title.png")
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_mode = "RGBA"
bpy.ops.render.render(write_still=True)
print("saved", sc.render.filepath)
