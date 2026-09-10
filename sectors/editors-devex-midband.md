# Sector survey: editors-devex (midband 1k-5k)

Account: `vulragrag-star` · refreshed `2026-09-08T17:38:01Z` · TS/JS/Zig DevEx slice · No fork/PR/comment.

Playbook lens: parser/path/formatter/LSP/bundler tooling with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 46 | No hard ban in common paths |
| disclosure | 1 | AI disclosure language |
| hostility_risk | 1 | Hostility-adjacent |

Proceed: **35** · Leave: **13**.

## PROCEED candidates (contrib fit)

| Repo | Stars | Policy | Why fit | Sample bug class |
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
| `quick-lint/quick-lint-js` | 1592 | silent | Fast JS diagnostics engine; parse/diag edges | JS parse/diag edge + tests |
| `ktock/buildg` | 1502 | silent | Interactive Dockerfile debugger; path/IDE edges | Dockerfile path/breakpoint edge + Go tests |
| `dave/dst` | 1438 | silent | Decorated Go syntax tree; rewrite/fidelity edges | Go AST rewrite/fidelity edge + tests |
| `oxc-project/tsgolint` | 1412 | silent | Type-aware oxlint companion; rule/path edges | TS lint rule/path edge + tests |
| `quarylabs/sqruff` | 1383 | silent | Fast SQL formatter/linter; dialect/parse edges | SQL dialect/format edge + Rust tests |
| `fables-tales/rubyfmt` | 1230 | silent | Ruby autoformatter | Ruby format fixture edge + Rust tests |
| `jdx/hk` | 1153 | disclosure | Git hooks + project lints; config/path — AGENTS AI-assisted mention | hook config/path edge + tests — disclose if agent-assisted |
| `tombi-toml/tombi` | 1107 | silent | TOML formatter/linter/LSP | TOML format/lint/LSP edge + Rust tests |

## LEAVE list

| Repo | Stars | Policy | Reason |
|---|---:|---|---|
| `KDE/ghostwriter` | 4980 | silent | Markdown note UI app — weak parser/LSP hunk fit |
| `texstudio-org/texstudio` | 3620 | silent | Heavy LaTeX GUI — prefer LSP/formatter homes |
| `autozimu/LanguageClient-neovim` | 3565 | silent | Superseded/low-maintenance LSP client — prefer active LSP hosts |
| `rslint/rslint` | 2729 | silent | WIP abandoned (last push 2023) — not active product |
| `JamieMason/syncpack` | 2092 | hostility_risk | hostility_risk mentor-gated policy leave |
| `not-an-aardvark/lucky-commit` | 1991 | silent | Vanity commit-hash novelty — not DevEx product core |
| `zee-editor/zee` | 1804 | silent | Low-maintenance terminal editor (quiet since early 2025) |
| `rohit-px2/nvui` | 1742 | silent | Stale Neovim frontend (2023) — prefer goneovim/gnvim |
| `sakura-editor/sakura` | 1487 | silent | Niche Japanese Windows editor — weak outsider fit |
| `usagi-flow/evil-helix` | 1368 | silent | Helix fork — prefer upstream helix when in band |
| `PHPantom-dev/phpantom_lsp` | 1180 | silent | Very new/unknown PHP LSP — prefer mago |
| `noib3/nvim-oxi` | 1138 | silent | Rust Neovim bindings library — not editor product |
| `kkoomen/vim-doge` | 1058 | silent | Docstring generator plugin — weak playbook hunk class |

## Sector synthesis

- Refreshed after TS/JS/Zig DevEx product slice.
- No tracker comments/forks/third-party PRs.
- scored_at: `2026-09-08T17:38:01Z`

## Deepen pass (2026-09-09, +44 scored)

Account: `vulragrag-star` · Curated product midband slice from remaining unscored editors-devex leftovers + `gh search` fills · Policy via `raw.githubusercontent.com` · **32** proceed / **12** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 42, 'hard_ban': 1, 'disclosure': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `mg979/vim-visual-multi` | 4885 | silent | Multiple cursors for Vim/Neovim; selection/path edges | multi-cursor selection edge + Vim tests |
| `anordal/shellharden` | 4803 | silent | Corrective bash syntax highlighter/linter; parse/quoting edges | bash parse/quoting/syntax edge + Rust tests |
| `akinomyoga/ble.sh` | 4692 | silent | Bash Line Editor with syntax highlighting; completion/path edges | readline/completion/path edge + shell tests |
| `numToStr/Comment.nvim` | 4668 | silent | Smart Neovim comment plugin; filetype/path edges | comment filetype/path edge + Lua tests |
| `amperser/proselint` | 4574 | silent | Prose linter; rule/path/config edges | lint rule/path/config edge + tests |
| `LuaLS/lua-language-server` | 4365 | silent | Lua language server; LSP/diagnose/path edges | LSP diagnose/path/workspace edge + tests |
| `jiangmiao/auto-pairs` | 4194 | silent | Vim bracket/quote auto-pair plugin; insert edges | auto-pair insert/edge + Vim tests |
| `prettier/prettier-eslint` | 4101 | silent | Prettier then ESLint --fix bridge; config/path edges | format bridge/config/path edge + tests |
| `xcpretty/xcpretty` | 4036 | silent | xcodebuild output formatter; parse/format edges | xcodebuild parse/format edge + Ruby tests |
| `VonHeikemen/lsp-zero.nvim` | 3977 | silent | Neovim LSP starter kit; config/LSP wiring edges | LSP config/wiring edge + Lua tests |
| `mason-org/mason-lspconfig.nvim` | 3945 | silent | mason.nvim ↔ lspconfig bridge; install/config edges | LSP install/config bridge edge + Lua tests |
| `verilator/verilator` | 3916 | silent | SystemVerilog simulator + lint; parse/lint edges | SV parse/lint/diag edge + C++ tests |
| `swiftlang/sourcekit-lsp` | 3903 | silent | Swift/C-family language server; LSP/index/path edges | Swift LSP index/path edge + tests |
| `erikw/tmux-powerline` | 3837 | silent | Hackable tmux status bar; segment/config/path edges | tmux segment/config/path edge + shell tests |
| `nvimdev/lspsaga.nvim` | 3802 | silent | Neovim LSP UX improvements; UI/LSP path edges | LSP UI/path/handler edge + Lua tests |
| `prettier/eslint-plugin-prettier` | 3652 | silent | ESLint plugin running Prettier; rule/config edges | eslint prettier rule/config edge + tests |
| `stackrox/kube-linter` | 3503 | silent | Kubernetes YAML static analysis CLI; rule/path edges | k8s YAML lint rule/path edge + Go tests |
| `Kotlin/kotlin-lsp` | 3501 | silent | Kotlin language server + VS Code plugin; LSP/path edges | Kotlin LSP/path/analyze edge + tests |
| `adrienverge/yamllint` | 3455 | silent | YAML linter; rule/path/config edges | YAML lint rule/path edge + Python tests |
| `Shougo/dein.vim` | 3420 | silent | Vim/Neovim plugin manager; install/path/config edges | plugin install/path/config edge + Vim tests |
| `prabirshrestha/vim-lsp` | 3415 | silent | Async LSP client for Vim/Neovim; protocol/path edges | LSP client protocol/path edge + Vim tests |
| `waf/CSharpRepl` | 3342 | silent | C# REPL with syntax highlighting; eval/path edges | REPL eval/path/completion edge + C# tests |
| `csscomb/csscomb.js` | 3334 | silent | CSS coding-style formatter; option/parse edges | CSS format option/parse edge + JS tests |
| `artempyanykh/marksman` | 3330 | silent | Markdown language server; link/path/wiki edges | markdown LSP link/path edge + F# tests |
| `dbcli/litecli` | 3297 | silent | SQLite CLI with completion/syntax; path/completion edges | SQL completion/path edge + Python tests |
| `nvimtools/none-ls.nvim` | 3261 | silent | null-ls reloaded — inject linters/formatters as LSP; source/path edges | null-ls source/path/config edge + Lua tests |
| `haydenbleasel/ultracite` | 3255 | silent | Zero-config linter/formatter; rule/path edges | lint/format config/path edge + TS tests |
| `textlint/textlint` | 3178 | silent | Pluggable natural-language linter; rule/path edges | textlint rule/path edge + TS tests |
| `editorconfig/editorconfig-vim` | 3166 | silent | EditorConfig Vim plugin; indent/path/config edges | editorconfig path/indent edge + Vim tests |
| `tmux-plugins/tmux-yank` | 3105 | silent | tmux clipboard yank plugin; buffer/path edges | tmux yank/buffer edge + shell tests |
| `denoland/deno_lint` | 1584 | silent | Fast JS/TS linter (Deno); rule/parse edges | JS/TS lint rule/parse edge + Rust tests |
| `fcsonline/tmux-thumbs` | 1097 | silent | tmux copy matcher (fingers successor); match/path edges | tmux match/copy edge + Rust tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `zufuliu/notepad4` | 4977 | silent | Windows Scintilla notepad fork — weak outsider systems/LSP fit |
| `callumlocke/json-formatter` | 4130 | silent | Browser JSON pretty-print extension — not editor/LSP product core |
| `ekzhang/rustpad` | 4076 | silent | Collaborative web code editor — weak playbook path/parser hunk class |
| `jdorn/sql-formatter` | 3845 | silent | Legacy PHP SQL formatter — prefer sqruff/sqlfluff-class homes already mapped |
| `cknadler/vim-anywhere` | 3767 | silent | Launch-Vim-anywhere shell utility — low-maintenance / weak product farm |
| `mrcjkb/rustaceanvim` | 3108 | hard_ban | CONTRIBUTING no-LLM / NO-AI hard ban — leave |
| `mileszs/ack.vim` | 3076 | silent | ack.vim superseded by ripgrep/telescope ecosystem — weak fresh hunk surface |
| `qt-creator/qt-creator` | 3070 | disclosure | Heavy Qt IDE process — prefer smaller LSP/formatter homes even with CLAUDE disclosure |
| `cpeditor/cpeditor` | 2177 | silent | Competitive-programming IDE niche — weak general DevEx farm |
| `dzhou121/gonvim` | 1779 | silent | Superseded Neovim GUI — prefer goneovim/gnvim already on midband proceed |
| `royqh1979/RedPanda-CPP` | 1451 | silent | Niche lightweight C++ IDE — prefer clangd/qt-creator-adjacent only if needed |
| `eval-exec/neomacs` | 1186 | silent | WIP Neo Emacs — too early/unknown for midband first homes |

Notes: Prefer LSP/formatter/linter/tmux-DevEx product surfaces with regression tests. Leave heavy IDEs, Windows notepad forks, browser JSON extensions, collaborative web pads, competitive-programming IDEs, superseded ack.vim/gonvim, and WIP Neo Emacs. `mrcjkb/rustaceanvim` is a hard no-LLM leave.

## Famous editors/shells midband subset (2026-09-10, +2 from famous editors-shells pass)

Midband (1k–5k★) subset · **2** proceed / **0** leave.

### PROCEED

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `gyscos/cursive` | 4846 | silent | Rust TUI library; focus/layout/event edges | focus/layout/event edge + Rust tests |
| `urwid/urwid` | 3017 | silent | Python console UI library; widget/layout edges | widget/layout edge + Python tests |

### LEAVE

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| — | | | none |

