#!/usr/bin/env python3
"""Build sector-balanced SHORTLIST.md from data/scored.jsonl."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

# Quotas sum to 100. Heavier on primary farm + freshly deepened DevEx.
SECTOR_QUOTAS = {
    "cli-systems": 18,
    "devops-build": 14,
    "editors-devex": 14,
    "python-tooling": 12,
    "databases-storage": 12,
    "compilers-runtimes": 10,
    "networking-distributed": 10,
    "security-crypto": 10,
}


def load_scored(path: Path) -> list[dict]:
    by: dict[str, dict] = {}
    if not path.exists():
        return []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        name = row.get("full_name")
        if name:
            by[name] = row
    return list(by.values())


def rank_key(row: dict) -> tuple:
    stars = int(row.get("stars") or 0)
    has_hint = 1 if (row.get("bug_class_hint") or "").strip() else 0
    # Prefer rows with a concrete bug-class hint, then stars.
    return (-has_hint, -stars, row.get("full_name") or "")


def pick_balanced(proceed: list[dict], quotas: dict[str, int], limit: int) -> list[dict]:
    by_sector: dict[str, list[dict]] = defaultdict(list)
    for row in proceed:
        by_sector[row.get("sector") or "unknown"].append(row)
    for sector in by_sector:
        by_sector[sector].sort(key=rank_key)

    chosen: list[dict] = []
    chosen_names: set[str] = set()
    for sector, quota in quotas.items():
        for row in by_sector.get(sector, [])[:quota]:
            name = row["full_name"]
            if name in chosen_names:
                continue
            chosen.append(row)
            chosen_names.add(name)

    # Fill remainder from leftover proceed (any sector), still preferring hint+stars.
    if len(chosen) < limit:
        rest = [r for r in proceed if r["full_name"] not in chosen_names]
        rest.sort(key=rank_key)
        for row in rest:
            if len(chosen) >= limit:
                break
            chosen.append(row)
            chosen_names.add(row["full_name"])

    # Stable presentation: stars desc within the selected set.
    chosen.sort(key=lambda r: (-int(r.get("stars") or 0), r.get("full_name") or ""))
    return chosen[:limit]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scored", type=Path, default=Path("data/scored.jsonl"))
    ap.add_argument("--out", type=Path, default=Path("SHORTLIST.md"))
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()

    rows = load_scored(args.scored)
    proceed = [r for r in rows if r.get("proceed")]
    selected = pick_balanced(proceed, SECTOR_QUOTAS, args.limit)

    sector_counts: dict[str, int] = defaultdict(int)
    for r in selected:
        sector_counts[r.get("sector") or "?"] += 1
    mix = ", ".join(f"{k}={v}" for k, v in sorted(sector_counts.items(), key=lambda kv: -kv[1]))

    lines = [
        f"# Shortlist ({len(selected)} / target {args.limit})",
        "",
        "Sector-balanced from proceed rows (not pure megastar sort). "
        "Primary weight: cli-systems + devops-build; elevated editors-devex after TS/JS DevEx scoring; "
        "security-crypto and databases-storage no longer token-represented.",
        "",
        f"Mix: {mix}",
        "",
        "| Repo | Stars | Sector | Policy | Bug class hint |",
        "|---|---|---|---|---|",
    ]
    for r in selected:
        lines.append(
            f"| {r.get('full_name', '')} | {r.get('stars', '')} | {r.get('sector', '')} | "
            f"{r.get('policy', '')} | {r.get('bug_class_hint', '')} |"
        )
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.out} n={len(selected)} mix={dict(sector_counts)}")


if __name__ == "__main__":
    main()
