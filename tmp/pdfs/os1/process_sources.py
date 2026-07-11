from __future__ import annotations

import re
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont
from rapidocr_onnxruntime import RapidOCR


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "tmp" / "pdfs" / "os1"
TEXT_DIR = OUT / "text"
CONTACT_DIR = OUT / "contacts"


def safe_name(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "_", value).strip("_")[:72]


def sources() -> list[tuple[str, Path, range | None]]:
    chapter_dir = ROOT / "408" / "操作系统基础考点讲解" / "第一章 计算机系统概述"
    items: list[tuple[str, Path, range | None]] = [
        ("教材_2026操作系统_第1章", ROOT / "408" / "2026操作系统.pdf", range(12, 48)),
    ]
    for path in sorted(chapter_dir.glob("*.pdf"), key=lambda item: item.name):
        items.append((f"基础_{path.stem}", path, None))
    items.extend(
        [
            (
                "阶段_OS期中试卷及答案解析",
                ROOT / "408" / "操作系统基础考点讲解" / "OS期中试卷及答案解析（学员版）.pdf",
                None,
            ),
            (
                "阶段_OS期末试卷及答案解析",
                ROOT / "408" / "操作系统基础考点讲解" / "OS期末试卷及答案解析（学员版）.pdf",
                None,
            ),
            (
                "强化_操作系统强化结课考试",
                ROOT / "408" / "操作系统强化" / "操作系统强化【结课考试】.pdf",
                None,
            ),
            (
                "强化_操作系统强化结课考试答案",
                ROOT / "408" / "操作系统强化" / "操作系统强化【结课考试+答案】.pdf",
                None,
            ),
            (
                "强化_操作系统历年真题合集",
                ROOT / "408" / "操作系统强化" / "操作系统历年真题合集.pdf",
                None,
            ),
        ]
    )
    return items


def render_page(page: fitz.Page, dpi: int = 110) -> Image.Image:
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def make_contact(images: list[tuple[int, Image.Image]], output: Path) -> None:
    thumb_width = 920
    margin = 22
    label_height = 38
    columns = 2
    rows = 3
    prepared: list[tuple[int, Image.Image]] = []
    max_height = 0
    for page_no, image in images:
        ratio = thumb_width / image.width
        resized = image.resize((thumb_width, round(image.height * ratio)), Image.Resampling.LANCZOS)
        prepared.append((page_no, resized))
        max_height = max(max_height, resized.height)
    canvas = Image.new(
        "RGB",
        (columns * thumb_width + (columns + 1) * margin, rows * (max_height + label_height) + (rows + 1) * margin),
        "white",
    )
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=24)
    for index, (page_no, image) in enumerate(prepared):
        col = index % columns
        row = index // columns
        x = margin + col * (thumb_width + margin)
        y = margin + row * (max_height + label_height + margin)
        draw.text((x, y), f"PDF p{page_no}", fill="black", font=font)
        canvas.paste(image, (x, y + label_height))
    canvas.save(output, quality=92)


def main() -> None:
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    ocr = RapidOCR(intra_op_num_threads=4, inter_op_num_threads=1)
    ocr_targets = {12, 26, 27, 29, 37, 40, 41, 46}
    manifest: list[str] = []
    total_pages = 0
    total_ocr = 0

    for source_index, (label, path, selected_pages) in enumerate(sources()):
        doc = fitz.open(path)
        indices = list(selected_pages if selected_pages is not None else range(doc.page_count))
        total_pages += len(indices)
        stem = f"{source_index:02d}_{safe_name(label)}"
        text_parts: list[str] = []
        contact_batch: list[tuple[int, Image.Image]] = []
        contact_index = 1
        source_ocr = 0

        for page_index in indices:
            page = doc[page_index]
            page_no = page_index + 1
            extracted = page.get_text("text").strip()
            image = render_page(page)
            needs_ocr = source_index == 0 and page_index in ocr_targets
            if needs_ocr:
                ocr_image = render_page(page, dpi=72)
                result, _ = ocr(ocr_image)
                recognized = "\n".join(item[1] for item in result) if result else ""
                if recognized.strip():
                    extracted = f"{extracted}\n[OCR]\n{recognized}".strip()
                source_ocr += 1
                total_ocr += 1
            text_parts.append(f"\n===== {label} | PDF p{page_no} =====\n{extracted}\n")
            contact_batch.append((page_no, image))
            if len(contact_batch) == 6:
                make_contact(contact_batch, CONTACT_DIR / f"{stem}_{contact_index:02d}.png")
                contact_batch = []
                contact_index += 1

        if contact_batch:
            make_contact(contact_batch, CONTACT_DIR / f"{stem}_{contact_index:02d}.png")

        (TEXT_DIR / f"{stem}.txt").write_text("".join(text_parts), encoding="utf-8")
        manifest.append(
            f"{source_index:02d}\t{label}\tpages={len(indices)}\tocr={source_ocr}\tpath={path.relative_to(ROOT).as_posix()}"
        )
        print(manifest[-1], flush=True)

    manifest.append(f"TOTAL\tpages={total_pages}\tocr={total_ocr}")
    (OUT / "manifest.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(manifest[-1], flush=True)


if __name__ == "__main__":
    main()
