# Sector survey: editors-devex

Account: `vulragrag-star` · Input: `survey/raw/editors-devex.jsonl` (noisy) · Sampled **38** repos deep from `notes/editors-devex-raw/` · No fork/PR/comment · Atlas sync slice.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **parser / path / quoting / formatter / git-DevEx bugs with regression tests** (not docs farm, not GFI spam, not sprite/ebook/map/whiteboard editors).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 32 | No hard ban found in common CONTRIBUTING/AI paths (normalized) |
| disclosure | 3 | Neovim AGENTS.md AI-assisted trailer; Astral AI_POLICY; Zed soft disclosure |
| hard_ban | 1 | `fish-shell/fish-shell` generative-AI ban |
| agentscan | 2 | `withastro/astro`, `nuxt/nuxt` |
| hostility_risk | 0 | — |

Proceed: **19** · Leave: **19** · Scored lines in `survey/scored.jsonl` + atlas `data/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `neovim/neovim` | 102213 | disclosure | AGENTS.md AI-assisted trailer; famous terminal editor + LSP host | path/option/Lua runtime edge + tests |
| `zed-industries/zed` | 89921 | disclosure | soft CONTRIBUTING disclosure; human judgement; max 3 open PRs | path/project-open or config parse + tests |
| `coder/code-server` | 79236 | silent | VS Code in browser; no hard AI ban | path/proxy/config edge + tests |
| `mozilla/pdf.js` | 53846 | silent | PDF parser surface with unit-test culture; product code home | parser edge + unit tests |
| `prettier/prettier` | 52240 | silent | Opinionated formatter with strong fixture tests | parser/printer fixture edge + tests |
| `astral-sh/ruff` | 49545 | disclosure | PR template links astral AI_POLICY; human-in-loop required | rule/path/config parse edge + tests |
| `git-lfs/git-lfs` | 14476 | silent | Git LFS; path/transfer edges | pointer/path/transfer edge + tests |
| `coder/coder` | 14399 | silent | Cloud IDE / workspace product; no hard ban for human-owned fixes | CLI flag/path/template edge + tests |
| `jonas/tig` | 13327 | silent | Classic text-mode git UI; parse/path surface | argv/path/config edge + tests |
| `mawww/kakoune` | 11049 | silent | Terminal editor; copyright-waiver empty commit; no AI ban | command/parser quoting edge + tests |
| `a-h/templ` | 10532 | silent | Go HTML templ + LSP; discuss before large PRs | template parser/escape edge + tests |
| `AGWA/git-crypt` | 9895 | silent | Transparent git encryption; small C++ surface | filter path/smudge edge + tests |
| `evilmartians/lefthook` | 8786 | silent | Git hooks manager; config/path/glob edges | hook path/glob/config edge + tests |
| `j178/prek` | 8382 | silent | Rust pre-commit alternative; hook config edges | config/path edge + tests |
| `bensadeh/tailspin` | 7959 | silent | Terminal log highlighter; small Rust CLI | regex/theme/path config edge + tests |
| `rust-lang/rustfmt` | 6961 | silent | Rust formatter; usable with correctness bar | config/edition/path edge + tests |
| `facebook/pyrefly` | 6946 | silent | Python LSP/typechecker; claim issues first; Meta CLA | config/path/parse edge + tests |
| `dominikh/go-tools` | 6890 | silent | Staticcheck / go-tools analyzer product | analyzer/pattern edge + tests |
| `tummychow/git-absorb` | 5715 | silent | git commit --fixup automation; small Rust CLI | path/commit selection edge + tests |

### Tier notes

**Best first homes (small testable parser/path/format hunks):**

1. `jonas/tig` — text-mode git UI; argv/path/config edges; silent policy.
2. `prettier/prettier` — formatter fixtures; treat as silent usable home with tests.
3. `astral-sh/ruff` — snapshot-test culture; follow Astral AI_POLICY (human-in-loop, no autonomous agents).
4. `evilmartians/lefthook` / `j178/prek` / `tummychow/git-absorb` — git-hook/absorb CLIs.
5. `a-h/templ` / `mozilla/pdf.js` — template/PDF parser edges + unit tests.
6. `dominikh/go-tools` (Staticcheck) — analyzer false ± with tests.
7. `neovim/neovim` — high impact; generic AI-assisted trailer only; small runtime/path/Lua edges.

**Proceed with process friction:** `zed-industries/zed` (PR cap / no vibe-coded); `facebook/pyrefly` (claim issues / Meta CLA); `coder/coder` & `coder/code-server` (large IDE surface).

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `github/gitignore` | 175660 | silent | template dump not product |
| `airbnb/javascript` | 148182 | silent | style-guide docs farm |
| `excalidraw/excalidraw` | 131388 | silent | whiteboard UI-heavy |
| `toeverything/AFFiNE` | 72315 | silent | Notion-like UI farm |
| `withastro/astro` | 62394 | agentscan | AgentScan adopter org |
| `upstash/context7` | 61763 | silent | docs-context farm risk |
| `nuxt/nuxt` | 60830 | agentscan | AgentScan adopter org |
| `adam-p/markdown-here` | 60247 | silent | stale extension / weak fit |
| `ChromeDevTools/chrome-devtools-mcp` | 51318 | silent | MCP satellite |
| `cypress-io/cypress` | 51034 | silent | prefer lint/format homes first |
| `fish-shell/fish-shell` | 34151 | hard_ban | generative AI ban in CONTRIBUTING.rst |
| `xi-editor/xi-editor` | 19819 | silent | low-maintenance research editor |
| `vnotex/vnote` | 12936 | silent | note app farm risk |
| `mapeditor/tiled` | 12874 | silent | game map editor wrong class |
| `antirez/kilo` | 9112 | silent | teaching editor not product target |
| `LibreSprite/LibreSprite` | 8359 | silent | niche fork |
| `kunchenguid/no-mistakes` | 8350 | silent | not famous systems product core |
| `Sigil-Ebook/Sigil` | 6948 | silent | ebook editor wrong class |
| `LongSoft/UEFITool` | 5660 | silent | niche firmware tool |

## Sector synthesis

- **Hard exclude:** `fish-shell/fish-shell` — CONTRIBUTING.rst generative-AI ban. Do not argue on their tracker.
- **AgentScan:** `withastro/astro`, `nuxt/nuxt` — leave entire circles.
- **Fit theme:** formatters (Prettier, Ruff, rustfmt), git DevEx (tig, lefthook, prek, git-absorb, git-lfs, git-crypt), terminal editors (neovim, kakoune), parser homes (templ, pdf.js, Staticcheck).
- **Avoid:** template/style-guide farms (`gitignore`, `airbnb/javascript`); UI farms (AFFiNE, excalidraw, vnote); wrong-class editors (Sigil, Tiled, LibreSprite, UEFITool); MCP/docs satellites; dormant/toy editors (xi, kilo).
- **Secondary to CLI/build thesis:** editors-devex formatters + git tooling are strong secondary homes after systems CLI; keep SQL/storage as another secondary band.

## Method notes

- Stars/policy confirmation from `notes/editors-devex-raw/*.json`; proceed/leave judgments from operator classification (2026-09-08 atlas sync).
- Policy normalization: silent_with/no_contributing → silent; disclosure_or_mention → disclosure.
- No tracker comments, forks, or third-party PRs from this survey pass.
- scored_at: `2026-09-08T07:58:00Z`
