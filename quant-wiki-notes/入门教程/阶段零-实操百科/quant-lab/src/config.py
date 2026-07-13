from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
STRATEGIES = ROOT / "strategies"

# Teaching defaults — override in scripts or strategy specs.
DEFAULT_START = "20200101"
DEFAULT_END = "20231231"
DEFAULT_ADJUST = "qfq"
DEFAULT_SYMBOL = "000001"
