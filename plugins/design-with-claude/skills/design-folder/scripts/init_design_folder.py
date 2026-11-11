"""Create (or complete) the design folder: root CLAUDE.md, templates, and one folder per brand.
Safe to re-run: never overwrites files that already exist.

Usage: python3 init_design_folder.py "<root path>" ["Brand A" "Brand B" ...]
"""
import sys, shutil, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TPL = HERE / "templates"
BRAND_TPL = HERE.parent / "brand-setup" / "references" / "brand-template.md"
SUBDIRS = ["logos", "fuentes", "fotos", "referencias/instagram", "referencias/cliente", "estilos", "3d", "piezas"]


def write_if_missing(path: Path, text: str):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print("created", path)


def main():
    root = Path(sys.argv[1]).expanduser()
    brands = sys.argv[2:]
    root.mkdir(parents=True, exist_ok=True)
    write_if_missing(root / "CLAUDE.md", (TPL / "root-CLAUDE.md").read_text(encoding="utf-8"))
    (root / "_plantillas").mkdir(exist_ok=True)
    for src, name in ((TPL / "brand-CLAUDE.md", "CLAUDE.md"), (BRAND_TPL, "brand.md")):
        if src.exists():
            write_if_missing(root / "_plantillas" / name, src.read_text(encoding="utf-8"))
    today = datetime.date.today().isoformat()
    for b in brands:
        d = root / b
        for s in SUBDIRS:
            (d / s).mkdir(parents=True, exist_ok=True)
        claude = (TPL / "brand-CLAUDE.md").read_text(encoding="utf-8").replace("{{BRAND}}", b)
        write_if_missing(d / "CLAUDE.md", claude)
        if BRAND_TPL.exists():
            write_if_missing(d / "brand.md", BRAND_TPL.read_text(encoding="utf-8").replace("[Brand name]", b))
        write_if_missing(d / "historial.md", f"# Historial — {b}\n\n{today} — Carpeta creada.\n\n## Ideas\n- \n")
        write_if_missing(d / "pendientes-code.md",
                         f"# Pendientes para Claude Code — {b}\n\n"
                         "Formato de cada tarea:\n\n"
                         "- [ ] **Qué**: …  **Con qué**: rutas de entrada  **Entregar**: qué archivos y dónde  **Skill**: …\n")
    print("ok:", root)


if __name__ == "__main__":
    main()
