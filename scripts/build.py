"""Build the image library: SVG files + JSON API.

Usage:  python3 scripts/build.py          (then: node scripts/render_png.cjs)
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from art import render  # noqa: E402
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
    print(f"built {len(items)} images, {len(PLANNED)} planned")


if __name__ == "__main__":
    main()
