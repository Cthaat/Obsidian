from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tmp.pdfs.math01 import process_chapter as base


base.OUT = Path(__file__).resolve().parent
base.PAGE_DIR = base.OUT / "pages"
base.CONTACT_DIR = base.OUT / "contacts"
base.START_PAGE = 169
base.END_PAGE = 190


if __name__ == "__main__":
    base.main()
