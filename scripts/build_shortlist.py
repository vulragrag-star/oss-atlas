#!/usr/bin/env python3
"""Build SHORTLIST.md from data/scored.jsonl."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scored", type=Path, default=Path("data/scored.jsonl"))
    ap.add_argument("--out", type=Path, default=Path("SHORTLIST.md"))
    ap.add_argument("--limit", type=int, default=100)
    args = ap.parse_args()
    rows = []
    if args.scored.exists():
        for line in args.scored.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    proceed = sorted([r for r in rows if r.get("proceed")], key=lambda r: -int(r.get("stars") or 0))[:args.limit]
    lines = [f"# Shortlist ({len(proceed)} / target {args.limit})", "", "| Repo | Stars | Sector | Policy | Bug class hint |", "|---|---|---|---|---|"]
    for r in proceed:
        lines.append(f"| {r.get('full_name','')} | {r.get('stars','')} | {r.get('sector','')} | {r.get('policy','')} | {r.get('bug_class_hint','')} |")
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.out} n={len(proceed)}")

if __name__ == "__main__":
    main()
