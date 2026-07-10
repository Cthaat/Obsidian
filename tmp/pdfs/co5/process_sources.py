from __future__ import annotations

import json
import math
import re
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont
from rapidocr_onnxruntime import RapidOCR


ROOT = Path(r"C:\Code\Obsidian")
SOURCE_ROOT = ROOT / "408"
OUT = ROOT / "tmp" / "pdfs" / "co5"
TEXT_DIR = OUT / "text"
CONTACT_DIR = OUT / "contacts"


def safe_slug(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "_", value).strip("_")
    return value[:70]


def page_image(page: fitz.Page, scale: float) -> Image.Image:
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def ocr_page(engine: RapidOCR, page: fitz.Page) -> str:
    image = page_image(page, 1.55)
    result, _ = engine(image)
    if not result:
        return ""
    rows = sorted(result, key=lambda item: (min(p[1] for p in item[0]), min(p[0] for p in item[0])))
    return "\n".join(item[1] for item in rows if len(item) >= 2)


def make_contacts(doc: fitz.Document, pages: list[int], slug: str, display_name: str) -> list[str]:
    paths: list[str] = []
    per_sheet = 6
    cell_w, cell_h = 720, 1020
    header_h = 40
    font = ImageFont.load_default()
    for sheet_index, start in enumerate(range(0, len(pages), per_sheet), 1):
        selected = pages[start : start + per_sheet]
        sheet = Image.new("RGB", (cell_w * 2, (cell_h + header_h) * 3), (225, 225, 225))
        draw = ImageDraw.Draw(sheet)
        for slot, page_index in enumerate(selected):
            image = page_image(doc[page_index], 0.8)
            image.thumbnail((cell_w - 20, cell_h - 20), Image.Resampling.LANCZOS)
            x = (slot % 2) * cell_w
            y = (slot // 2) * (cell_h + header_h)
            draw.rectangle((x, y, x + cell_w - 1, y + header_h - 1), fill="white")
            label = f"{display_name} | PDF p{page_index + 1}"
            draw.text((x + 10, y + 12), label, fill="black", font=font)
            sheet.paste(image, (x + (cell_w - image.width) // 2, y + header_h + 5))
        path = CONTACT_DIR / f"{slug}_{sheet_index:02d}.png"
        sheet.save(path, optimize=True)
        paths.append(str(path.relative_to(OUT)))
    return paths


def build_sources() -> list[dict]:
    textbook = SOURCE_ROOT / "27王道《计算机组成原理》高清带书签.pdf"
    chapter_dir = SOURCE_ROOT / "计算机组成原理基础考点讲解" / "第五章 中央处理器"
    sources: list[dict] = [
        {
            "phase": "textbook",
            "path": textbook,
            "pages": list(range(206, 285)),
            "force_ocr": True,
        }
    ]
    for path in sorted(chapter_dir.glob("*.pdf")):
        sources.append({"phase": "base", "path": path, "pages": None, "force_ocr": False})
    stage_dir = SOURCE_ROOT / "计算机组成原理基础考点讲解"
    for name in (
        "计算机组成原理期中试卷及答案解析（学员版）.pdf",
        "计算机组成原理期末试卷及答案解析（学员版）.pdf",
    ):
        sources.append({"phase": "stage", "path": stage_dir / name, "pages": None, "force_ocr": True})
    reinforce = SOURCE_ROOT / "组成原理强化"
    for path in (
        reinforce / "课件" / "计组P4_一堆指令的执行.pdf",
        reinforce / "课件" / "计组P5_一条指令的执行.pdf",
        reinforce / "【录播】五段式指令流水线题型总结.pdf",
        reinforce / "计组强化课考试_试题+答案.pdf",
    ):
        sources.append({"phase": "reinforce", "path": path, "pages": None, "force_ocr": True})
    return sources


def main() -> None:
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    engine = RapidOCR()
    manifest: list[dict] = []
    phase_stats: dict[str, dict[str, int]] = {}

    for source_index, source in enumerate(build_sources()):
        path: Path = source["path"]
        if not path.exists():
            raise FileNotFoundError(path)
        doc = fitz.open(path)
        pages = source["pages"] or list(range(doc.page_count))
        slug = f"{source_index:02d}_{safe_slug(path.stem)}"
        text_path = TEXT_DIR / f"{slug}.txt"
        expected_contacts = math.ceil(len(pages) / 6)
        existing_contacts = sorted(CONTACT_DIR.glob(f"{slug}_*.png"))
        low_text_count = sum(len(doc[page_index].get_text("text").strip()) < 120 for page_index in pages)
        planned_ocr_count = len(pages) if source["force_ocr"] else low_text_count
        if text_path.exists() and len(existing_contacts) == expected_contacts:
            contacts = [str(item.relative_to(OUT)) for item in existing_contacts]
            entry = {
                "phase": source["phase"], "name": path.name, "path": str(path.relative_to(ROOT)),
                "selected_pages": len(pages), "document_pages": doc.page_count,
                "low_text_pages": low_text_count, "ocr_pages": planned_ocr_count,
                "text_file": str(text_path.relative_to(OUT)), "contacts": contacts, "reused": True,
            }
            manifest.append(entry)
            stats = phase_stats.setdefault(source["phase"], {"groups": 0, "pages": 0, "ocr": 0, "contacts": 0})
            stats["groups"] += 1; stats["pages"] += len(pages); stats["ocr"] += planned_ocr_count; stats["contacts"] += len(contacts)
            print(json.dumps(entry, ensure_ascii=False), flush=True)
            continue
        blocks: list[str] = []
        ocr_count = 0
        low_text_count = 0
        for page_index in pages:
            extracted = doc[page_index].get_text("text").strip()
            needs_ocr = source["force_ocr"] or len(extracted) < 120
            if len(extracted) < 120:
                low_text_count += 1
            recognized = ""
            if needs_ocr:
                recognized = ocr_page(engine, doc[page_index])
                ocr_count += 1
            blocks.append(f"\n===== PDF p{page_index + 1} =====\n[EXTRACTED]\n{extracted}\n[OCR]\n{recognized}\n")
        text_path.write_text("".join(blocks), encoding="utf-8")
        contacts = make_contacts(doc, pages, slug, path.stem)
        entry = {
            "phase": source["phase"], "name": path.name, "path": str(path.relative_to(ROOT)),
            "selected_pages": len(pages), "document_pages": doc.page_count,
            "low_text_pages": low_text_count, "ocr_pages": ocr_count,
            "text_file": str(text_path.relative_to(OUT)), "contacts": contacts,
        }
        manifest.append(entry)
        stats = phase_stats.setdefault(source["phase"], {"groups": 0, "pages": 0, "ocr": 0, "contacts": 0})
        stats["groups"] += 1; stats["pages"] += len(pages); stats["ocr"] += ocr_count; stats["contacts"] += len(contacts)
        print(json.dumps(entry, ensure_ascii=False), flush=True)

    summary = {
        "groups": len(manifest), "pages": sum(item["selected_pages"] for item in manifest),
        "ocr_pages": sum(item["ocr_pages"] for item in manifest),
        "contacts": sum(len(item["contacts"]) for item in manifest), "phases": phase_stats,
    }
    (OUT / "manifest.json").write_text(
        json.dumps({"summary": summary, "sources": manifest}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"summary": summary}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
