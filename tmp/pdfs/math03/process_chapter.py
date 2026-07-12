from __future__ import annotations

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1] / "math01"
sys.path.insert(0, str(BASE_DIR))

import process_chapter as chapter


OUT = Path(__file__).resolve().parent
chapter.OUT = OUT
chapter.PAGE_DIR = OUT / "pages"
chapter.CONTACT_DIR = OUT / "contacts"
chapter.START_PAGE = 104
chapter.END_PAGE = 123


if __name__ == "__main__":
    chapter.main()
