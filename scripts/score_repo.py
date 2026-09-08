#!/usr/bin/env python3
"""Fetch lightweight policy file presence for one owner/repo."""
from __future__ import annotations
import argparse, json, subprocess

def gh_api(path: str) -> str:
    p = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""

def exists(owner, repo, path) -> bool:
    return bool(gh_api(f"repos/{owner}/{repo}/contents/{path}"))

def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("repo"); args = ap.parse_args()
    owner, name = args.repo.split("/", 1)
    meta = json.loads(gh_api(f"repos/{owner}/{name}") or "{}")
    print(json.dumps({
        "full_name": args.repo,
        "stars": meta.get("stargazers_count"),
        "archived": meta.get("archived"),
        "signals": {p: exists(owner, name, p) for p in ("CONTRIBUTING.md","AI_POLICY.md","AI.md","AGENTS.md")},
        "note": "Presence only — read bodies before proceed.",
    }, indent=2))

if __name__ == "__main__":
    main()
