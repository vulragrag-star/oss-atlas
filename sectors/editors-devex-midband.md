# Sector survey: editors-devex (midband 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/editors-devex-midband.jsonl` · Deep-sampled **46** real product repos via `raw.githubusercontent.com` policy files · Hard leaves respected · No fork/PR/comment · Band: `1k-5k`.

Playbook lens: famous main product (1k–5k★), not AgentScan, not hard AI ban, hunk class = **LSP / formatter / git UI / terminal-editor parser-path bugs with regression tests** (not TFT displays, games, ebook/map editors, vanity hash toys).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 45 | No hard ban found in common CONTRIBUTING/AI paths |
| disclosure | 1 | Explicit AI-assisted / disclosure language |

Proceed: **34** · Leave: **12** · Appended to `survey/scored.jsonl` with `band: "1k-5k"`.

## Hard leaves (playbook — even if outside this band sample)

- `fish-shell/fish-shell` — generative-AI ban (higher band; already scored leave)
- `withastro/astro`, `nuxt/nuxt` — AgentScan adopter orgs (higher band)
- Do not treat TFT/display/game/ebook editors in raw dump as DevEx product

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `tkellogg/dura` | 4430 | silent | Background git commit watcher; path/repo edges | git watch/path edge + Rust tests |
| `jmacdonald/amp` | 4127 | silent | Terminal text editor; command/path/config edges | editor command/path/config edge + Rust tests |
| `MaskRay/ccls` | 4087 | silent | C/C++/ObjC language server; xref/path/index edges | LSP index/path/compile_commands edge + tests |
| `github/git-sizer` | 4072 | silent | Git repo size metrics CLI; pack/path edges | git pack/path metric edge + Go tests |
| `dprint/dprint` | 4068 | silent | Pluggable multi-language formatter platform; fixture/path/config edges | formatter plugin/path/config edge + tests |
| `geany/geany` | 3706 | silent | Lightweight IDE; filetype/path/config edges | filetype/path/config edge + C tests |
| `Myriad-Dreamin/tinymist` | 3516 | silent | Typst language service; LSP/parse/path edges | Typst LSP/parse/path edge + tests |
| `carthage-software/mago` | 3428 | silent | PHP toolchain (lint/format/analyze); parse edges | PHP parse/lint/format edge + tests |
| `qltysh/qlty` | 3141 | silent | Universal lint/format/security CLI; config/path edges | lint plugin/path/config edge + tests |
| `willcrichton/flowistry` | 3071 | silent | Rust IDE focus plugin; span/path analysis edges | span/path analysis edge + Rust tests |
| `uncrustify/uncrustify` | 3068 | silent | Code beautifier; option/parse edges with strong config surface | format option/parse edge + C++ tests |
| `joshmedeski/sesh` | 2819 | silent | Smart tmux session manager; path/session edges | tmux session/path edge + Go tests |
| `akiyosi/goneovim` | 2624 | silent | Neovim GUI frontend; path/config/RPC edges | GUI path/config/RPC edge + Go tests |
| `kisielk/errcheck` | 2526 | silent | Go unchecked-error linter | Go AST visitor/path edge + tests |
| `raine/workmux` | 2391 | silent | git worktrees + tmux; path/worktree edges | worktree/path/tmux edge + tests |
| `tamasfe/taplo` | 2386 | silent | TOML toolkit (LSP/formatter/linter); parse edges | TOML parse/format/LSP edge + Rust tests |
| `JohnnyMorganz/StyLua` | 2287 | silent | Lua code formatter; fixture-test culture | Lua format fixture edge + Rust tests |
| `Feel-ix-343/markdown-oxide` | 2280 | silent | PKM Markdown language server | markdown LSP/path/wiki-link edge + tests |
| `liuchengxu/vim-clap` | 2144 | silent | Vim/Neovim fuzzy picker; path/provider edges | picker path/provider edge + Vim/Rust tests |
| `MordechaiHadad/bob` | 2141 | silent | Neovim version manager; path/install edges | install/path/version edge + Rust tests |
| `vhakulinen/gnvim` | 1958 | silent | Neovim GUI without web bloat; path/RPC edges | GUI path/RPC edge + Rust tests |
| `chipsalliance/verible` | 1931 | silent | SystemVerilog lint/format/parse suite | SV parse/lint/format edge + C++ tests |
| `MitMaro/git-interactive-rebase-tool` | 1883 | silent | Terminal git rebase sequence editor; path/todo edges | rebase todo/path edge + Rust tests |
| `candid82/joker` | 1769 | silent | Clojure interpreter + linter/formatter | Clojure lint/format edge + Go tests |
| `ycm-core/ycmd` | 1741 | silent | Completion/comprehension server; path/compile flags edges | completion path/flags edge + tests |
| `huacnlee/autocorrect` | 1628 | silent | Copywriting linter/formatter; rule/path edges | lint rule/path edge + Rust tests |
| `iwe-org/iwe` | 1626 | silent | Markdown knowledge-graph LSP; path/link edges | markdown link/path LSP edge + tests |
| `ktock/buildg` | 1502 | silent | Interactive Dockerfile debugger; path/IDE edges | Dockerfile path/breakpoint edge + Go tests |
| `dave/dst` | 1438 | silent | Decorated Go syntax tree; rewrite/fidelity edges | Go AST rewrite/fidelity edge + tests |
| `oxc-project/tsgolint` | 1412 | silent | Type-aware oxlint companion; rule/path edges | TS lint rule/path edge + tests |
| `quarylabs/sqruff` | 1383 | silent | Fast SQL formatter/linter; dialect/parse edges | SQL dialect/format edge + Rust tests |
| `fables-tales/rubyfmt` | 1230 | silent | Ruby autoformatter | Ruby format fixture edge + Rust tests |
| `jdx/hk` | 1153 | disclosure | Git hooks + project lints; config/path — AGENTS AI-assisted mention | hook config/path edge + tests — disclose if agent-assisted |
| `tombi-toml/tombi` | 1107 | silent | TOML formatter/linter/LSP | TOML format/lint/LSP edge + Rust tests |

### Tier notes

**Best first homes (small testable parser/path/format hunks):** start near the top of the proceed table; one home at a time; stay after a merge.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `KDE/ghostwriter` | 4980 | silent | Markdown note UI app — weak parser/LSP hunk fit |
| `texstudio-org/texstudio` | 3620 | silent | Heavy LaTeX GUI — prefer LSP/formatter homes |
| `autozimu/LanguageClient-neovim` | 3565 | silent | Superseded/low-maintenance LSP client — prefer active LSP hosts |
| `rslint/rslint` | 2729 | silent | WIP abandoned (last push 2023) — not active product |
| `not-an-aardvark/lucky-commit` | 1991 | silent | Vanity commit-hash novelty — not DevEx product core |
| `zee-editor/zee` | 1804 | silent | Low-maintenance terminal editor (quiet since early 2025) |
| `rohit-px2/nvui` | 1742 | silent | Stale Neovim frontend (2023) — prefer goneovim/gnvim |
| `sakura-editor/sakura` | 1487 | silent | Niche Japanese Windows editor — weak outsider fit |
| `usagi-flow/evil-helix` | 1368 | silent | Helix fork — prefer upstream helix when in band |
| `PHPantom-dev/phpantom_lsp` | 1180 | silent | Very new/unknown PHP LSP — prefer mago |
| `noib3/nvim-oxi` | 1138 | silent | Rust Neovim bindings library — not editor product |
| `kkoomen/vim-doge` | 1058 | silent | Docstring generator plugin — weak playbook hunk class |

## Sector synthesis

- Midband (1k-5k) deep sample: **46** curated product repos.
- Proceed **34** / Leave **12**.
- Disclosure repos: `jdx/hk`.
- No AgentScan / fish-style / sqlite-agentic hits inside this midband sample (those hard leaves live in higher-star scored set).
- Method: policy files via `raw.githubusercontent.com` (CONTRIBUTING*/AI*/AGENTS*/PR templates); local AgentScan blacklist only.
- No fork / PR / tracker comment performed.

