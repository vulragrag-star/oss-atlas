#!/usr/bin/env python3
"""Harvest a high-star GitHub repository universe into JSONL via `gh api`."""
from __future__ import annotations
import argparse, json, subprocess, time, urllib.parse
from pathlib import Path

def gh_api(path: str) -> dict:
    p = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr or p.stdout)
    return json.loads(p.stdout)

def search(q: str, pages: int = 10) -> list[dict]:
    got, seen = [], set()
    for page in range(1, pages + 1):
        path = f"search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=100&page={page}"
        items = (gh_api(path).get("items") or [])
        if not items:
            break
        for it in items:
            full = it["full_name"]
            if full in seen or it.get("fork"):
                continue
            seen.add(full)
            got.append({
                "full_name": full,
                "stars": it["stargazers_count"],
                "language": it.get("language"),
                "description": (it.get("description") or "")[:240],
                "topics": it.get("topics") or [],
                "archived": it.get("archived", False),
                "default_branch": it.get("default_branch"),
                "html_url": it.get("html_url"),
                "pushed_at": it.get("pushed_at"),
            })
        if len(items) < 100:
            break
        time.sleep(0.7)
    return got

QUERIES = [
    "stars:>=20000 fork:false",
    "stars:>=20000 language:TypeScript fork:false",
    "stars:>=20000 language:JavaScript fork:false",
    "stars:>=20000 language:Zig fork:false",
    "stars:5000..19999 language:Rust fork:false",
    "stars:5000..19999 language:Go fork:false",
    "stars:5000..19999 language:C fork:false",
    "stars:5000..19999 language:C++ fork:false",
    "stars:5000..19999 language:Python fork:false",
    "stars:5000..19999 language:TypeScript fork:false",
    "stars:5000..19999 language:JavaScript fork:false",
    "stars:5000..19999 language:Zig fork:false",
    "stars:2000..4999 language:Rust fork:false",
    "stars:2000..4999 language:Go fork:false",
    "stars:2000..4999 language:C fork:false",
    "stars:2000..4999 language:C++ fork:false",
    "stars:2000..4999 language:Python fork:false",
    "stars:2000..4999 language:Shell fork:false",
    "stars:2000..4999 language:TypeScript fork:false",
    "stars:2000..4999 language:JavaScript fork:false",
    "stars:2000..4999 language:Zig fork:false",
    "stars:1000..1999 language:Rust fork:false",
    "stars:1000..1999 language:Go fork:false",
    "stars:1000..1999 language:C fork:false",
    "stars:1000..1999 language:C++ fork:false",
    "stars:1000..1999 language:Python fork:false",
    "stars:1000..1999 language:Shell fork:false",
    "stars:1000..1999 language:TypeScript fork:false",
    "stars:1000..1999 language:JavaScript fork:false",
    "stars:1000..1999 language:Zig fork:false",
]

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path("data/universe.jsonl"))
    ap.add_argument("--max", type=int, default=2500)
    args = ap.parse_args()
    seen, rows = set(), []
    for q in QUERIES:
        for r in search(q):
            if r["full_name"] in seen or r.get("archived"):
                continue
            seen.add(r["full_name"]); rows.append(r)
        print(f"{q}: total={len(seen)}")
        if len(seen) >= args.max:
            break
        time.sleep(0.5)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    rows.sort(key=lambda r: -r["stars"])
    args.out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    print(f"wrote {args.out} n={len(rows)}")

if __name__ == "__main__":
    main()
