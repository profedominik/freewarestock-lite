"""Build the image library: SVG files + JSON API.

Usage:  python3 scripts/build.py          (then: node scripts/render_png.cjs)
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from art import render  # noqa: E402
import art_a2  # noqa: E402,F401  (registers A2 drawings)
import art_b1  # noqa: E402,F401  (registers B1 drawings)
from vocab import WORDS, PLANNED  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SVG_DIR = ROOT / "images" / "svg"
API = ROOT / "api" / "v1"
LICENSE = {"id": "CC0-1.0", "name": "Creative Commons Zero v1.0 Universal (public domain)",
           "url": "https://creativecommons.org/publicdomain/zero/1.0/"}


def main():
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    (API / "images").mkdir(parents=True, exist_ok=True)
    items = []
    for i, w in enumerate(WORDS, 1):
        (SVG_DIR / f"{w['slug']}.svg").write_text(render(w["slug"], w["category"]), encoding="utf-8")
        item = {
            "id": i,
            **w,
            "status": "available",
            "license": LICENSE["id"],
            "width": 512,
            "height": 512,
            "files": {
                "svg": f"images/svg/{w['slug']}.svg",
                "png": f"images/png/{w['slug']}.png",
            },
            "api": f"api/v1/images/{w['slug']}.json",
        }
        items.append(item)
        (API / "images" / f"{w['slug']}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")

    levels = {}
    for it in items + PLANNED:
        lv = levels.setdefault(it["level"], {"available": 0, "planned": 0})
        lv["available" if it.get("status") == "available" else "planned"] += 1

    manifest = {
        "name": "FreewareStock Lite",
        "description": "Free (CC0) illustrations of basic vocabulary for language learning.",
        "version": 1,
        "license": LICENSE,
        "count": len(items),
        "levels": levels,
        "categories": sorted({it["category"] for it in items}),
        "images": items,
        "planned": PLANNED,
    }
    text = json.dumps(manifest, ensure_ascii=False, indent=2)
    (API / "images.json").write_text(text, encoding="utf-8")
    # A JS copy lets index.html work when opened straight from disk (file://)
    (ROOT / "data" / "manifest.js").write_text("window.FREEWARESTOCK = " + text + ";\n", encoding="utf-8")
    write_gallery(items)
    print(f"built {len(items)} images, {len(PLANNED)} planned")


def write_gallery(items, cols=6):
    """GALLERY.md: every image visible directly on GitHub, grouped by level and topic."""
    out = ["# Gallery", "",
           f"All **{len(items)}** illustrations, CC0 (public domain). Click an image to open the SVG.", "",
           "Levels: " + " · ".join(f"[{lv}](#level-{lv.lower()})" for lv in sorted({i['level'] for i in items})), ""]
    for lv in sorted({i["level"] for i in items}):
        group = [i for i in items if i["level"] == lv]
        out += [f"## Level {lv}", "", f"{len(group)} images", ""]
        for cat in sorted({i["category"] for i in group}):
            row = [i for i in group if i["category"] == cat]
            out += [f"### {cat.capitalize()} ({len(row)})", ""]
            out += ["| " + " | ".join([" "] * cols) + " |", "|" + "---|" * cols]
            for k in range(0, len(row), cols):
                chunk = row[k:k + cols]
                cells = [f'<a href="{i["files"]["svg"]}"><img src="{i["files"]["png"]}" width="110" alt="{i["word"]}"></a><br>'
                         f'<b>{i["word"]}</b><br><sub>{i["translations"]["es"]} · {i["translations"]["fr"]} · {i["translations"]["de"]}</sub>'
                         for i in chunk]
                cells += [" "] * (cols - len(chunk))
                out.append("| " + " | ".join(cells) + " |")
            out.append("")
    (ROOT / "GALLERY.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
