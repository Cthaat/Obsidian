from __future__ import annotations

import json
import os
import re
from pathlib import Path

import fitz
import numpy as np
from PIL import Image, ImageDraw
from rapidocr_onnxruntime import RapidOCR


ROOT = Path(r"C:\Code\Obsidian")
OUT = ROOT / "tmp" / "pdfs" / "os4"
TEXT_DIR = OUT / "text"
CONTACT_DIR = OUT / "contacts"
TEXT_DIR.mkdir(parents=True, exist_ok=True)
CONTACT_DIR.mkdir(parents=True, exist_ok=True)


def safe_name(value: str) -> str:
    value = re.sub(r"[<>:\"/\\|?*+]", "_", value)
    return re.sub(r"\s+", "_", value).strip("._")


def visible_chars(value: str) -> int:
    return len(re.findall(r"[A-Za-z0-9\u4e00-\u9fff]", value))


base_dir = ROOT / "408" / "操作系统基础考点讲解"
chapter_dir = base_dir / "第四章 文件管理"
reinforce_dir = ROOT / "408" / "操作系统强化"

sources: list[dict[str, object]] = [
    {
        "label": "00_教材_2026操作系统_第4章",
        "path": ROOT / "408" / "2026操作系统.pdf",
        "start": 264,
        "end": 317,
    }
]

for index, path in enumerate(sorted(chapter_dir.glob("*.pdf")), start=1):
    sources.append(
        {
            "label": f"{index:02d}_基础_{path.stem}",
            "path": path,
            "start": 1,
            "end": None,
        }
    )

stage_paths = [
    base_dir / "OS期中试卷及答案解析（学员版）.pdf",
    base_dir / "OS期末试卷及答案解析（学员版）.pdf",
]
for path in stage_paths:
    sources.append(
        {
            "label": f"{len(sources):02d}_阶段_{path.stem}",
            "path": path,
            "start": 1,
            "end": None,
        }
    )

reinforce_names = [
    "操作系统P3+P4_文件系统骚图.pdf",
    "操作系统P4【凌乱手稿】_文件系统骚图.pdf",
    "操作系统强化【结课考试】.pdf",
    "操作系统强化【结课考试+答案】.pdf",
    "操作系统历年真题合集.pdf",
]
for name in reinforce_names:
    path = reinforce_dir / name
    sources.append(
        {
            "label": f"{len(sources):02d}_强化_{path.stem}",
            "path": path,
            "start": 1,
            "end": None,
        }
    )

ocr = RapidOCR()
manifest: list[dict[str, object]] = []
start_group = int(os.environ.get("START_GROUP", "0"))

for source in sources[start_group:]:
    path = Path(source["path"])
    if not path.exists():
        raise FileNotFoundError(path)

    doc = fitz.open(path)
    start = int(source["start"])
    end = int(source["end"] or doc.page_count)
    end = min(end, doc.page_count)
    label = str(source["label"])
    page_texts: list[str] = []
    page_images: list[tuple[int, Image.Image]] = []
    ocr_pages: list[int] = []

    for page_no in range(start, end + 1):
        page = doc[page_no - 1]
        extracted = page.get_text("text").strip()
        pix = page.get_pixmap(matrix=fitz.Matrix(1.15, 1.15), alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

        if visible_chars(extracted) < 90:
            result, _ = ocr(np.asarray(image))
            if result:
                ocr_text = "\n".join(str(item[1]) for item in result if len(item) >= 2)
                if visible_chars(ocr_text) > visible_chars(extracted):
                    extracted = ocr_text
            ocr_pages.append(page_no)

        page_texts.append(f"\n===== PDF p{page_no} =====\n{extracted}\n")
        page_images.append((page_no, image))

    text_path = TEXT_DIR / f"{safe_name(label)}.txt"
    text_path.write_text("".join(page_texts), encoding="utf-8")

    contact_paths: list[str] = []
    for part_no, offset in enumerate(range(0, len(page_images), 6), start=1):
        batch = page_images[offset : offset + 6]
        cell_w = max(image.width for _, image in batch)
        cell_h = max(image.height for _, image in batch) + 34
        sheet = Image.new("RGB", (cell_w * 3, cell_h * 2), "white")
        draw = ImageDraw.Draw(sheet)
        for cell_no, (page_no, image) in enumerate(batch):
            x = (cell_no % 3) * cell_w
            y = (cell_no // 3) * cell_h
            draw.text((x + 8, y + 8), f"PDF p{page_no}", fill="black")
            sheet.paste(image, (x, y + 30))
        contact_path = CONTACT_DIR / f"{safe_name(label)}_{part_no:02d}.png"
        sheet.save(contact_path, optimize=True)
        contact_paths.append(str(contact_path.relative_to(ROOT)))

    manifest.append(
        {
            "label": label,
            "path": str(path.relative_to(ROOT)),
            "start": start,
            "end": end,
            "pages": end - start + 1,
            "ocr_pages": ocr_pages,
            "text": str(text_path.relative_to(ROOT)),
            "contacts": contact_paths,
        }
    )
    print(
        f"{label}: pages={end - start + 1}, ocr={len(ocr_pages)}, "
        f"contacts={len(contact_paths)}",
        flush=True,
    )

(OUT / f"manifest_{start_group:02d}.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
)
summary = {
    "groups": len(manifest),
    "pages": sum(int(item["pages"]) for item in manifest),
    "ocr_pages": sum(len(item["ocr_pages"]) for item in manifest),
    "contacts": sum(len(item["contacts"]) for item in manifest),
}
(OUT / f"summary_{start_group:02d}.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(json.dumps(summary, ensure_ascii=False), flush=True)
