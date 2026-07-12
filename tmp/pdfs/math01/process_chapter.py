from __future__ import annotations

import json
import re
import sys
from concurrent.futures import ProcessPoolExecutor
from io import BytesIO
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont
from rapidocr_onnxruntime import RapidOCR


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
PDF = ROOT / "考研数学" / "27张宇基础30讲高数.pdf"
OUT = Path(__file__).resolve().parent
PAGE_DIR = OUT / "pages"
CONTACT_DIR = OUT / "contacts"
START_PAGE = 6
END_PAGE = 80
SCALE = 1.7
OCR_WIDTH = 700
OCR_WORKERS = 1
CONTACT_SIZE = 4
THUMB_WIDTH = 940
MARGIN = 24
LABEL_HEIGHT = 38


def font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path(r"C:\Windows\Fonts\msyh.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def ocr_lines(result: list | None) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in result or []:
        if len(item) < 3:
            continue
        text = re.sub(r"\s+", " ", str(item[1])).strip()
        if text:
            rows.append({"text": text, "score": round(float(item[2]), 4)})
    return rows


def example_ids(text: str) -> list[str]:
    found: set[str] = set()
    patterns = [
        r"(?:例|题)\s*([1１][\.．·][0-9０-９]{1,2})",
        r"(?<![0-9])([1１][\.．][0-9０-９]{1,2})(?![0-9])",
    ]
    for pattern in patterns:
        for match in re.findall(pattern, text):
            normalized = match.translate(str.maketrans("０１２３４５６７８９．", "0123456789."))
            found.add(normalized)
    return sorted(found, key=lambda value: tuple(int(x) for x in value.split(".")))


_OCR: RapidOCR | None = None


def init_ocr() -> None:
    global _OCR
    _OCR = RapidOCR()


def recognize_page(payload: tuple[int, int, str]) -> dict[str, object]:
    global _OCR
    if _OCR is None:
        _OCR = RapidOCR()
    pdf_page, print_page, image_path = payload
    image = Image.open(image_path).convert("RGB")
    if image.width > OCR_WIDTH:
        ratio = OCR_WIDTH / image.width
        image = image.resize((OCR_WIDTH, int(image.height * ratio)))
    result, elapsed = _OCR(image)
    lines = ocr_lines(result)
    joined = "\n".join(str(row["text"]) for row in lines)
    return {
        "pdf_page": pdf_page,
        "print_page": print_page,
        "image": image_path,
        "elapsed": elapsed,
        "line_count": len(lines),
        "avg_score": round(sum(float(row["score"]) for row in lines) / len(lines), 4) if lines else None,
        "examples": example_ids(joined),
        "lines": lines,
    }


def make_contact(items: list[dict[str, object]], index: int) -> Path:
    thumbs: list[tuple[int, int, Image.Image]] = []
    for item in items:
        path = Path(str(item["image"]))
        image = Image.open(path).convert("RGB")
        ratio = THUMB_WIDTH / image.width
        image = image.resize((THUMB_WIDTH, int(image.height * ratio)))
        thumbs.append((int(item["pdf_page"]), int(item["print_page"]), image))

    rows = (len(thumbs) + 1) // 2
    row_heights = []
    for row in range(rows):
        row_items = thumbs[row * 2 : row * 2 + 2]
        row_heights.append(max(img.height for _, _, img in row_items) + LABEL_HEIGHT)
    width = MARGIN * 3 + THUMB_WIDTH * 2
    height = MARGIN * (rows + 1) + sum(row_heights)
    sheet = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(sheet)
    label_font = font(23)
    y = MARGIN
    for row in range(rows):
        row_items = thumbs[row * 2 : row * 2 + 2]
        for col, (pdf_page, print_page, image) in enumerate(row_items):
            x = MARGIN + col * (THUMB_WIDTH + MARGIN)
            draw.rectangle((x, y, x + THUMB_WIDTH, y + LABEL_HEIGHT), fill=(242, 242, 242))
            draw.text((x + 10, y + 7), f"PDF p{pdf_page} / 印刷页 {print_page}", fill="black", font=label_font)
            sheet.paste(image, (x, y + LABEL_HEIGHT))
        y += row_heights[row] + MARGIN
    output = CONTACT_DIR / f"math01_{index:02d}.jpg"
    sheet.save(output, quality=88, optimize=True)
    return output


def main() -> None:
    PAGE_DIR.mkdir(parents=True, exist_ok=True)
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    render_jobs: list[tuple[int, int, str]] = []
    with fitz.open(PDF) as doc:
        for pdf_page in range(START_PAGE, END_PAGE + 1):
            image_path = PAGE_DIR / f"p{pdf_page:03d}.jpg"
            if not image_path.exists():
                page = doc[pdf_page - 1]
                pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), alpha=False)
                image = Image.open(BytesIO(pix.tobytes("png"))).convert("RGB")
                image.save(image_path, quality=91, optimize=True)
            render_jobs.append((pdf_page, pdf_page - 5, str(image_path)))
    print(f"rendered {len(render_jobs)} pages", flush=True)

    pages: list[dict[str, object]] = []
    with ProcessPoolExecutor(max_workers=OCR_WORKERS, initializer=init_ocr) as executor:
        for item in executor.map(recognize_page, render_jobs, chunksize=1):
            pages.append(item)
            print(f"processed PDF p{item['pdf_page']}: lines={item['line_count']} examples={item['examples']}", flush=True)
    pages.sort(key=lambda item: int(item["pdf_page"]))

    contacts = []
    for offset in range(0, len(pages), CONTACT_SIZE):
        contacts.append(str(make_contact(pages[offset : offset + CONTACT_SIZE], offset // CONTACT_SIZE + 1)))

    evidence = {
        "pdf": str(PDF),
        "range": [START_PAGE, END_PAGE],
        "page_count": len(pages),
        "contact_count": len(contacts),
        "contacts": contacts,
        "pages": pages,
    }
    (OUT / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    with (OUT / "ocr.txt").open("w", encoding="utf-8") as handle:
        for item in pages:
            handle.write(f"\n===== PDF p{item['pdf_page']} / 印刷页 {item['print_page']} =====\n")
            for row in item["lines"]:
                handle.write(str(row["text"]) + "\n")
    summary = {
        "page_count": len(pages),
        "contact_count": len(contacts),
        "ocr_line_count": sum(int(item["line_count"]) for item in pages),
        "example_pages": {str(item["pdf_page"]): item["examples"] for item in pages if item["examples"]},
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
