from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_report(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8"))


def risk_flags(report: dict[str, Any], max_dd_limit: float = 0.25) -> list[str]:
    """Teaching heuristics — not investment advice."""
    flags: list[str] = []
    mdd = report.get("max_drawdown")
    if mdd is not None and mdd <= -abs(max_dd_limit):
        flags.append(f"max_drawdown {mdd:.2%} at/under limit {-abs(max_dd_limit):.0%}")
    tr = report.get("total_return")
    bh = report.get("buy_hold_return")
    if tr is not None and bh is not None and tr < bh:
        flags.append("underperformed buy_hold over sample (not necessarily bad)")
    turn = report.get("avg_turnover")
    if turn is not None and turn > 0.2:
        flags.append(f"avg_turnover high ({turn:.3f}) — cost sensitivity check")
    if report.get("engine", "").startswith("factor") and "pit_note" not in report:
        flags.append("factor-like engine without pit_note field")
    if not report.get("disclaimer"):
        flags.append("missing disclaimer field")
    return flags


def format_summary(report: dict[str, Any], max_dd_limit: float = 0.25) -> str:
    lines = [
        f"engine: {report.get('engine')}",
        f"total_return: {report.get('total_return')}",
        f"buy_hold_return: {report.get('buy_hold_return')}",
        f"max_drawdown: {report.get('max_drawdown')}",
        f"n_days: {report.get('n_days')}",
        f"avg_turnover: {report.get('avg_turnover')}",
        f"avg_gross_exposure: {report.get('avg_gross_exposure')}",
    ]
    flags = risk_flags(report, max_dd_limit=max_dd_limit)
    lines.append("flags:" if flags else "flags: (none)")
    lines.extend(f"  - {f}" for f in flags)
    return "\n".join(lines)
