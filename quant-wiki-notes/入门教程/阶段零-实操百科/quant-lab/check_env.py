"""Environment sanity check. Run from quant-lab root: python check_env.py"""
from __future__ import annotations

import sys


def main() -> int:
    print("Python", sys.version.replace("\n", " "))
    try:
        import numpy as np
        import pandas as pd
        import matplotlib

        print("numpy", np.__version__)
        print("pandas", pd.__version__)
        print("matplotlib", matplotlib.__version__)
    except Exception as e:
        print("core import failed:", e)
        return 1

    try:
        import akshare as ak

        print("akshare", getattr(ak, "__version__", "ok"))
    except Exception as e:
        print("akshare import failed:", e)

    try:
        import backtrader as bt

        print("backtrader", getattr(bt, "__version__", "ok"))
    except Exception as e:
        print("backtrader not installed (optional):", e)

    print("ENV OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
