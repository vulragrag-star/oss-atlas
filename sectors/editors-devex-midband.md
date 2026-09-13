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

## Product deepen midband subset (2026-09-11, +15 scored)

Account: `vulragrag-star` · Curated editor/LSP/formatter/bundler/notebook product homes still missing after famous-editors + midband · Policy via `raw.githubusercontent.com` · **12** proceed / **3** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 13, 'disclosure': 1, 'agentscan': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `pulsar-edit/pulsar` | 4156 | silent | Community Atom fork editor; package/path/config edges | package/path/config edge + JS tests |
| `haskell/haskell-language-server` | 2955 | disclosure | Haskell LSP; cradle/path — AI policy template | HLS cradle/path edge + Haskell tests — disclose AI |
| `typescript-language-server/typescript-language-server` | 2561 | silent | TS language server wrapper; LSP/path edges | LSP/path/config edge + TS tests |
| `eclipse-jdtls/eclipse.jdt.ls` | 2438 | silent | Java language server; classpath/path edges | Java LSP classpath/path edge + Java tests |
| `scalameta/metals` | 2329 | silent | Scala language server; build/path edges | Scala LSP/build/path edge + Scala tests |
| `clangd/clangd` | 2284 | silent | C/C++ language server packaging; compile_commands/path edges | LSP compile_commands/path edge + tests |
| `fwcd/kotlin-language-server` | 2043 | silent | Kotlin LSP; compile/path edges | Kotlin LSP/path edge + Kotlin tests |
| `Shopify/ruby-lsp` | 2039 | silent | Ruby language server; indexing/path edges | Ruby LSP/index/path edge + Ruby tests |
| `phpactor/phpactor` | 1925 | silent | PHP language server/refactor; path/index edges | PHP refactor/path edge + PHP tests |
| `sourcegraph/zoekt` | 1882 | silent | Code search engine; index/path edges | index/path/query edge + Go tests |
| `elixir-lsp/elixir-ls` | 1776 | silent | Elixir language server; mix/path edges | Elixir LSP/mix/path edge + Elixir tests |
| `redhat-developer/yaml-language-server` | 1519 | silent | YAML LSP; schema/path edges | YAML schema/path edge + TS tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `stackblitz/webcontainer-core` | 4635 | silent | Browser Node runtime infra — not editor hunk farm |
| `sveltejs/language-tools` | 1444 | agentscan | AgentScan org (sveltejs) — leave |
| `hashicorp/terraform-ls` | 1202 | silent | Terraform LSP — devops-build sector adjacency; leave for that farm |

Notes: Prefer midband LSP (yaml/kotlin/phpactor/typescript-language-server/clangd packaging) and search/index (zoekt). Leave terraform-ls (devops adjacency) and AgentScan svelte language-tools.

## Midband product deepen (2026-09-11, +70 scored)

Account: `vulragrag-star` · Curated editors-devex midband (1k–5k★) LSP/formatter/editor/Neovim-product/VS Code/bundler homes still missing after prior editors product deepen · Policy via `raw.githubusercontent.com` · **47** proceed / **23** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 65, 'disclosure': 1, 'agentscan': 2, 'hard_ban': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `mermaid-js/mermaid-cli` | 4998 | silent | Mermaid diagram CLI; config/path/render edges with fixture culture | mermaid CLI config/path/render edge + tests |
| `lokalise/i18n-ally` | 4895 | silent | VS Code i18n tooling; locale/path/key edges | i18n key/path/locale edge + extension tests |
| `sublimehq/package_control` | 4884 | silent | Sublime package manager; install/path/channel edges | package install/path/channel edge + tests |
| `microsoft/vscode-python` | 4634 | silent | Official Python VS Code extension; env/path/LSP edges | Python env/path/LSP edge + extension tests |
| `vuejs/eslint-plugin-vue` | 4591 | silent | Official Vue ESLint plugin; rule/AST/path edges | Vue lint rule/AST/path edge + tests |
| `fallow-rs/fallow` | 4462 | silent | TS/JS static analysis CLI; style/path edges | static analysis path/style edge + Rust tests |
| `ibhagwan/fzf-lua` | 4435 | silent | Neovim fuzzy finder product; provider/path edges | picker provider/path edge + Lua tests |
| `L3MON4D3/LuaSnip` | 4426 | silent | Neovim snippet engine product; snippet/path edges | snippet parse/path edge + Lua tests |
| `kylechui/nvim-surround` | 4295 | silent | Neovim surround product; delimiter/operator edges | surround delimiter/operator edge + Lua tests |
| `golang/vscode-go` | 4263 | silent | Official Go VS Code extension; gopls/path edges | Go gopls/path/env edge + extension tests |
| `junegunn/vim-easy-align` | 4238 | silent | Vim alignment plugin with clear text/op edges | align delimiter/range edge + Vim tests |
| `folke/flash.nvim` | 4233 | silent | Neovim navigation product; label/motion edges | flash label/motion edge + Lua tests |
| `windwp/nvim-autopairs` | 4092 | silent | Neovim autopairs product; pair/rule edges | autopair rule/edge + Lua tests |
| `mvdan/gofumpt` | 4074 | silent | Stricter gofmt; format fixture edges | gofumpt format fixture edge + Go tests |
| `uber-go/nilaway` | 3903 | silent | Go nil static analysis; analyzer/path edges | nil analysis path/diag edge + Go tests |
| `nvim-orgmode/orgmode` | 3875 | disclosure | Orgmode for Neovim; parse/agenda/path — AGENTS AI-assisted disclosure | org parse/agenda/path edge + Lua tests — disclose if agent-assisted |
| `curlpipe/ox` | 3741 | silent | Terminal text editor; command/path/config edges | editor command/path/config edge + Rust tests |
| `charmbracelet/glamour` | 3688 | silent | CLI markdown stylesheet renderer; style/path edges | markdown render style/path edge + Go tests |
| `tailwindlabs/tailwindcss-intellisense` | 3472 | silent | Tailwind VS Code tooling; class/path/config edges | Tailwind class/path/config edge + extension tests |
| `web-infra-dev/rsbuild` | 3376 | silent | Rspack-based build tool; config/path/plugin edges | bundler config/path/plugin edge + tests |
| `vadimcn/codelldb` | 3295 | silent | Native debugger VS Code extension; path/breakpoint edges | debugger path/breakpoint edge + tests |
| `yzhang-gh/vscode-markdown` | 3285 | silent | Markdown All in One VS Code; preview/path edges | markdown preview/path/TOC edge + extension tests |
| `nvim-neotest/neotest` | 3119 | silent | Neovim test runner framework; adapter/path edges | test adapter/path edge + Lua tests |
| `athasdev/athas` | 3055 | silent | Cross-platform code editor; path/git/config edges | editor path/git/config edge + tests |
| `mtshiba/pylyzer` | 2856 | silent | Python analyzer + language server; type/path edges | Python LSP/type/path edge + Rust tests |
| `wellle/targets.vim` | 2642 | silent | Vim text-object product; object/edge selection | text-object selection edge + Vim tests |
| `redhat-developer/vscode-java` | 2295 | silent | Java language support for VS Code; JDT/path edges | Java JDT/path edge + extension tests |
| `neurocyte/flow` | 2213 | silent | Programmer text editor (Zig); command/path edges | editor command/path edge + Zig tests |
| `dotenv-linter/dotenv-linter` | 2102 | silent | dotenv linter CLI; rule/path edges | env lint rule/path edge + Rust tests |
| `sbdchd/neoformat` | 2047 | silent | Neovim/Vim format runner; formatter/path edges | format runner/path edge + Vim tests |
| `latex-lsp/texlab` | 2014 | silent | LaTeX language server; build/path/xref edges | LaTeX LSP build/path/xref edge + Rust tests |
| `castwide/solargraph` | 2007 | silent | Ruby language server; type/path edges | Ruby LSP type/path edge + tests |
| `ilai-deutel/kibi` | 1942 | silent | Minimal text editor; command/path edges | editor command/path edge + Rust tests |
| `liuchengxu/vista.vim` | 1934 | silent | LSP/tag viewer for Vim/Neovim; symbol/path edges | symbol view/path edge + Vim tests |
| `andymass/vim-matchup` | 1926 | silent | Enhanced match navigation; syntax/match edges | match/syntax edge + Vim tests |
| `bmewburn/vscode-intelephense` | 1859 | silent | PHP IntelliSense VS Code; symbol/path edges | PHP symbol/path edge + extension tests |
| `OlaProeis/Ferrite` | 1805 | silent | Markdown/JSON/YAML/TOML editor; parse/path edges | structured text parse/path edge + Rust tests |
| `sublimelsp/LSP` | 1797 | silent | Sublime LSP client; server/path/config edges | LSP client server/path/config edge + tests |
| `gabotechs/dep-tree` | 1723 | silent | Dependency graph CLI for keeping codebases decoupled; graph/path edges | dep graph/path edge + Go tests |
| `michaelb/sniprun` | 1709 | silent | Neovim code runner plugin; interpreter/path edges | sniprun interpreter/path edge + tests |
| `astral-sh/ruff-vscode` | 1671 | silent | Official Ruff VS Code extension; lint/format/path edges | ruff lint/format/path edge + extension tests |
| `Dart-Code/Dart-Code` | 1605 | silent | Dart/Flutter VS Code; analyzer/path edges | Dart analyzer/path edge + extension tests |
| `mattn/efm-langserver` | 1554 | silent | General-purpose LSP wrapper for linters/formatters; config/path edges | efm config/linter/path edge + Go tests |
| `denoland/vscode_deno` | 1548 | silent | Deno VS Code extension; path/config edges | Deno path/config edge + extension tests |
| `rvben/rumdl` | 1485 | silent | Markdown linter/formatter CLI; rule/path edges | markdown lint/format edge + Rust tests |
| `nix-community/nixd` | 1481 | silent | Nix language server; eval/path edges | Nix LSP eval/path edge + tests |
| `kristoff-it/superhtml` | 1370 | silent | HTML validator/formatter/LSP; parse edges | HTML parse/format/LSP edge + Zig tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `microsoft/tsdoc` | 4963 | silent | Doc-comment standard/spec — not a product CLI/LSP home |
| `junegunn/goyo.vim` | 4687 | silent | Distraction-free UI skin — prefer product LSP/formatter homes |
| `biomejs/gritql` | 4591 | agentscan | AgentScan adopter org (biomejs) — leave |
| `microsoft/codetour` | 4573 | silent | Code tour recorder — weak playbook hunk class |
| `akinsho/bufferline.nvim` | 4366 | silent | Bufferline UI chrome — prefer product LSP/formatter/picker homes |
| `rolldown/tsdown` | 4254 | hard_ban | PR template NO-AI — leave |
| `rust-lang/rust.vim` | 4184 | silent | Vim syntax pack — prefer rust-analyzer homes |
| `trivago/prettier-plugin-sort-imports` | 3950 | silent | Prettier plugin satellite — prefer prettier/dprint hosts |
| `pangloss/vim-javascript` | 3784 | silent | Syntax/indent pack — prefer LSP/formatter products |
| `jsx-eslint/eslint-plugin-jsx-a11y` | 3615 | silent | A11y ESLint plugin — prefer product linter/LSP homes |
| `unjs/unplugin` | 3605 | agentscan | AgentScan adopter — leave |
| `DisposaBoy/GoSublime` | 3400 | silent | Legacy Sublime Go plugin — prefer vscode-go/gopls |
| `amilajack/eslint-plugin-compat` | 3183 | silent | Compat ESLint plugin — weak systems hunk fit |
| `sublimehq/Packages` | 3018 | silent | Shipped Sublime syntax packs — not outsider product target |
| `azat-io/eslint-plugin-perfectionist` | 2920 | silent | Sorting ESLint plugin — prefer eslint core/plugin hosts with clearer tests |
| `godlygeek/tabular` | 2660 | silent | Legacy Vim align script — prefer vim-easy-align when needed |
| `RRethy/vim-illuminate` | 2467 | silent | Highlight companion plugin — skin-adjacent |
| `junegunn/limelight.vim` | 2451 | silent | Goyo companion UI skin — leave |
| `loeffel-io/ls-lint` | 2419 | hard_ban | AI_POLICY.md NO-AI — leave |
| `trishume/syntect` | 2413 | silent | Syntax-highlighting library — not editor/LSP product |
| `leafgarland/typescript-vim` | 1896 | silent | Syntax pack — prefer LSP homes |
| `gchp/iota` | 1661 | silent | Quiet/unmaintained terminal editor — prefer ox/kibi/flow |
| `ebkalderon/tower-lsp` | 1360 | silent | LSP framework library — prefer concrete language servers |

Notes: Prefer midband LSP/formatters/editors (texlab/solargraph/pylyzer/nixd/superhtml/rumdl/efm-langserver/ox/kibi/flow/Ferrite), product Neovim plugins (fzf-lua/LuaSnip/nvim-surround/neotest/neoformat/vista), VS Code language extensions (vscode-python/vscode-go/Dart-Code/ruff-vscode/vscode-java/intelephense), bundler/CLI (rsbuild/mermaid-cli/gofumpt/dotenv-linter). Disclosure: nvim-orgmode/orgmode. Leave AgentScan (biomejs/gritql, unjs/unplugin), hard_ban (rolldown/tsdown, loeffel-io/ls-lint), syntax packs, UI skins (goyo/limelight/bufferline), libraries (tower-lsp/syntect/tsdoc).

## Midband product deepen-2 (2026-09-12, +68 scored)

Account: `vulragrag-star` · Curated editors-devex midband (1k–5k★) LSP/formatter/editor/Neovim/VS Code/markdown leftovers after prior editors product deepens · Policy via `raw.githubusercontent.com` · **51** proceed / **17** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 66, 'agentscan': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `lukas-reineke/indent-blankline.nvim` | 4993 | silent | Neovim indent-guides product; scope/filetype/path edges with Lua tests | indent scope/filetype/path edge + Lua tests |
| `vuejs/vue-loader` | 4959 | silent | Official Vue webpack loader; SFC parse/path/loader edges | Vue SFC/loader path edge + tests |
| `fastmail/Squire` | 4909 | silent | HTML rich-text editor core; command/format edges | rich-text command/format edge + tests |
| `json-editor/json-editor` | 4904 | silent | JSON Schema form editor; schema/path/validate edges | JSON schema/path/validate edge + tests |
| `Tencent/cherry-markdown` | 4866 | silent | Markdown editor product; parse/render/path edges | markdown parse/render/path edge + tests |
| `suren-atoyan/monaco-react` | 4742 | silent | Monaco React wrapper; editor option/path edges | Monaco option/path edge + React tests |
| `martanne/vis` | 4713 | silent | Structural vi-like editor; command/path/regex edges | vis command/path/regex edge + tests |
| `oliverschwendener/ueli` | 4594 | silent | Cross-platform keystroke launcher; plugin/path/config edges | launcher plugin/path/config edge + TS tests |
| `amir9480/vscode-laravel-extra-intellisense` | 4213 | silent | Laravel VS Code intellisense; route/view/path edges | Laravel route/view/path edge + extension tests |
| `folke/todo-comments.nvim` | 4202 | silent | Neovim TODO highlight/search product; pattern/path edges | todo pattern/path edge + Lua tests |
| `m4xshen/hardtime.nvim` | 3842 | silent | Neovim motion-habit trainer with clear config surface | hardtime config/disabled-key edge + Lua tests |
| `ms-jpq/coq_nvim` | 3815 | silent | Neovim completion engine; source/path edges | completion source/path edge + Lua tests |
| `mdx-editor/editor` | 3673 | silent | MDX rich-text React editor; MDAST/Lexical parse edges — AGENTS guidance present | MDX/Lexical parse edge + Vitest |
| `OXY2DEV/markview.nvim` | 3635 | silent | Neovim markdown/Typst preview product; parse/path edges | markdown/Typst preview path edge + Lua tests |
| `privatenumber/esbuild-loader` | 3602 | silent | esbuild webpack loader; loader option/path edges | esbuild loader option/path edge + tests |
| `rcarriga/nvim-notify` | 3572 | silent | Neovim notification manager; config/render edges | notify config/render edge + Lua tests |
| `justinmk/vim-sneak` | 3533 | silent | Vim motion plugin; label/motion edges | sneak motion/label edge + Vim tests |
| `nvim-lua/plenary.nvim` | 3495 | silent | Neovim Lua stdlib used by plugins; path/async edges | plenary path/async edge + Lua tests |
| `lukakerr/Pine` | 3487 | silent | Native macOS markdown editor; open/path/render edges | markdown open/path/render edge + Swift tests |
| `pwntester/octo.nvim` | 3380 | silent | Neovim GitHub issues/PR UI; API/path edges | GitHub issue/PR path edge + Lua tests |
| `rcarriga/nvim-dap-ui` | 3372 | silent | nvim-dap UI product; layout/config edges | dap-ui layout/config edge + Lua tests |
| `nvim-treesitter/nvim-treesitter-context` | 3226 | silent | Treesitter sticky context; parser/path edges | treesitter context/path edge + tests |
| `Ionaru/easy-markdown-editor` | 3073 | silent | Embeddable markdown editor (EasyMDE); toolbar/parse edges | markdown toolbar/parse edge + JS tests |
| `kevinhwang91/nvim-ufo` | 2948 | silent | Neovim fold UI product; provider/path edges | fold provider/path edge + Lua tests |
| `uiwjs/react-md-editor` | 2926 | silent | React markdown editor with preview; parse/path edges | markdown parse/preview edge + React tests |
| `cweijan/vscode-database-client` | 2917 | silent | VS Code database client; connection/path/query edges | DB connection/path/query edge + extension tests |
| `jest-community/vscode-jest` | 2889 | silent | Official-adjacent Jest VS Code extension; config/path edges | Jest config/path edge + extension tests |
| `mfussenegger/nvim-lint` | 2782 | silent | Async Neovim lint runner; linter/path edges | linter config/path edge + Lua tests |
| `bash-lsp/bash-language-server` | 2777 | silent | Bash language server; parse/shellcheck/path edges | Bash LSP parse/path edge + TS tests |
| `tpope/vim-dispatch` | 2738 | silent | Vim async build/test dispatcher; compiler/path edges | dispatch compiler/path edge + Vim tests |
| `mhinz/vim-signify` | 2728 | silent | Vim VCS sign column; path/diff edges | signify path/diff edge + Vim tests |
| `romgrk/barbar.nvim` | 2727 | silent | Neovim tabline product; buffer/path edges | tabline buffer/path edge + Lua tests |
| `dvorka/mindforger` | 2718 | silent | Markdown thinking notebook/editor; note/path edges | notebook path/parse edge + C++ tests |
| `alefragnani/vscode-project-manager` | 2668 | silent | VS Code project manager; project path/config — AGENTS workflow present | project path/config edge + extension tests |
| `neomake/neomake` | 2665 | silent | Vim/Neovim async lint/make framework; maker/path edges | neomake maker/path edge + Vim tests |
| `ray-x/go.nvim` | 2659 | silent | Neovim Go tooling suite; gopls/path edges | Go gopls/path edge + Lua tests |
| `standard/eslint-config-standard` | 2645 | silent | JavaScript Standard Style ESLint config; rule/shareable edges | eslint config rule edge + tests |
| `j-hui/fidget.nvim` | 2594 | silent | Neovim LSP progress UI; notification/path edges | LSP progress UI edge + Lua tests |
| `imzbf/md-editor-v3` | 2587 | silent | Vue3 markdown editor; parse/toolbar/path edges | markdown parse/toolbar edge + TS tests |
| `estruyf/vscode-front-matter` | 2544 | silent | VS Code CMS/front-matter tooling; content/path edges | front-matter path/config edge + extension tests |
| `mhutchie/vscode-git-graph` | 2510 | silent | VS Code git graph UI; repo/path edges | git graph repo/path edge + extension tests |
| `formulahendry/vscode-code-runner` | 2437 | silent | VS Code code runner; executor/path/cwd edges | runner executor/path/cwd edge + extension tests |
| `btd/rollup-plugin-visualizer` | 2419 | silent | Rollup/Vite bundle visualizer; stats/path edges | bundle stats/path edge + tests |
| `ray-x/lsp_signature.nvim` | 2367 | silent | Neovim LSP signature hints; handler/path edges | LSP signature handler edge + Lua tests |
| `stevearc/aerial.nvim` | 2338 | silent | Neovim code outline window; symbol/path edges | outline symbol/path edge + Lua tests |
| `tim-koehler/Helm-Intellisense` | 2311 | silent | Helm VS Code intellisense; chart/path/value edges | Helm chart/path/values edge + extension tests |
| `prettier/pretty-quick` | 2288 | silent | Prettier git-staged runner; path/staged edges | pretty-quick staged/path edge + tests |
| `alefragnani/vscode-bookmarks` | 2168 | silent | VS Code bookmarks extension; line/path — AGENTS workflow present | bookmark line/path edge + extension tests |
| `markpluslabs/react-markplus` | 2115 | silent | React markdown editor/previewer; parse/path edges | markdown parse/preview edge + tests |
| `shd101wyy/vscode-markdown-preview-enhanced` | 2074 | silent | Markdown Preview Enhanced VS Code; preview/path — AGENTS guidance | markdown preview/path edge + extension tests |
| `francoismassart/eslint-plugin-tailwindcss` | 2073 | silent | Tailwind ESLint plugin; class/AST/path edges | Tailwind class/AST edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `babel/babel-loader` | 4835 | agentscan | AgentScan adopter org (babel) — leave circle |
| `CSSLint/csslint` | 4812 | silent | Stale CSS linter (quiet years) — prefer active Stylelint/Biome homes |
| `tonybaloney/vscode-pets` | 4172 | silent | Novelty pets UI — not DevEx product hunk class |
| `zbirenbaum/copilot.lua` | 4100 | silent | Copilot client plugin — AI completion product, not playbook farm |
| `EdenEast/nightfox.nvim` | 4073 | silent | Colorscheme — theme not parser/LSP/formatter farm |
| `jackMort/ChatGPT.nvim` | 3997 | silent | ChatGPT chat UI plugin — not contribution farm |
| `SilasMarvin/lsp-ai` | 3207 | silent | LLM language-server product — agentic AI LS, leave |
| `qax-os/goreporter` | 3120 | silent | Stale Go static-analysis suite — prefer active golangci/staticcheck homes |
| `rose-pine/neovim` | 3091 | silent | Colorscheme — theme not product farm |
| `material-extensions/vscode-material-icon-theme` | 2973 | silent | Icon theme — weak playbook hunk class |
| `nvimdev/dashboard-nvim` | 2873 | silent | Start-screen greeter — prefer editor/LSP/formatter homes |
| `nvim-tree/nvim-web-devicons` | 2717 | silent | Icon glyphs library — not editor product core |
| `palantir/python-language-server` | 2700 | silent | Superseded/archived Python LS — prefer python-lsp-server/basedpyright |
| `ellisonleao/gruvbox.nvim` | 2604 | silent | Colorscheme — theme not product farm |
| `goolord/alpha-nvim` | 2410 | silent | Greeter/start screen — weak playbook hunk class |
| `ggml-org/llama.vim` | 2170 | silent | LLM completion vim plugin — not playbook farm |
| `unjs/webpackbar` | 2090 | agentscan | AgentScan adopter org (unjs) — leave circle |

Notes: Prefer midband DevEx product homes (Bash/Python LS leftovers, Neovim lint/DAP/fold/outline/completion plugins, Vim dispatch/signify/sneak, VS Code Jest/project/git-graph/markdown/Laravel/Helm extensions, markdown/MDX/Monaco editors, webpack/esbuild/rollup/eslint adjacency). Leave AgentScan (babel-loader, unjs/webpackbar), themes/icons/greeters (nightfox/gruvbox/rose-pine/material-icons/web-devicons/dashboard/alpha), AI chat toys (ChatGPT.nvim/copilot.lua/llama.vim/lsp-ai/vscode-pets), superseded palantir python-LS, stale csslint/goreporter.

## Midband product deepen-3 (2026-09-13, +96 scored)

Account: `vulragrag-star` · Curated editors-devex midband TS/JS (1k–5k★) DevEx/CLI/LSP/formatter/bundler/editor product homes after universe TS/JS 1k–2k fill · Policy via `raw.githubusercontent.com` · **76** proceed / **20** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 91, 'hard_ban': 1, 'agentscan': 4}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `cssnano/cssnano` | 4976 | silent | PostCSS CSS minifier product; plugin/option/path edges | cssnano plugin/option edge + tests |
| `react-syntax-highlighter/react-syntax-highlighter` | 4676 | silent | React syntax-highlighter product; language/style/path edges | highlighter language/style edge + tests |
| `reactjs/react-codemod` | 4408 | silent | Official React codemod scripts; transform/path edges | codemod transform/path edge + tests |
| `unplugin/unplugin-vue-components` | 4293 | silent | Vue on-demand component auto-import unplugin; resolver/path edges | unplugin resolver/path edge + tests |
| `react-monaco-editor/react-monaco-editor` | 4207 | silent | Monaco React wrapper; editor option/path edges | Monaco option/path edge + React tests |
| `danvk/source-map-explorer` | 3932 | silent | Source-map bundle analyzer CLI; map/path edges | source-map path/analyze edge + tests |
| `webpack/sass-loader` | 3891 | silent | Official webpack Sass loader; include/path edges | sass-loader include/path edge + tests |
| `reactjs/react-docgen` | 3820 | silent | React component docgen CLI/lib; parse/path edges | docgen parse/path edge + tests |
| `unplugin/unplugin-auto-import` | 3796 | silent | Auto-import unplugin for Vite/Webpack/Rollup; resolver/path edges | auto-import resolver/path edge + tests |
| `rollup/plugins` | 3756 | silent | Official Rollup plugins monorepo; plugin option/path edges | rollup plugin option/path edge + tests |
| `mozilla/source-map` | 3724 | silent | Mozilla source-map consume/generate library; VLQ/path edges | source-map VLQ/path edge + tests |
| `antfu/vscode-file-nesting-config` | 3666 | silent | VS Code file-nesting config product; pattern/path edges | file-nesting pattern edge + tests |
| `surmon-china/vue-codemirror` | 3480 | silent | CodeMirror Vue component; option/path edges | CodeMirror Vue option/path edge + tests |
| `TypeStrong/ts-loader` | 3479 | silent | TypeScript webpack loader; config/path edges | ts-loader config/path edge + tests |
| `bcherny/json-schema-to-typescript` | 3348 | silent | JSON Schema→TS codegen CLI; schema/path edges | schema→TS path edge + tests |
| `YousefED/typescript-json-schema` | 3266 | silent | TS→JSON Schema generator; type/path edges | TS→schema type/path edge + tests |
| `stoplightio/spectral` | 3205 | silent | OpenAPI/AsyncAPI JSON/YAML linter CLI; rule/path edges | spectral rule/path edge + tests |
| `remirror/remirror` | 3035 | silent | ProseMirror React toolkit; extension/command edges | remirror extension/command edge + tests |
| `zh-lx/code-inspector` | 3019 | silent | Click-to-IDE source inspector; path/loader edges | code-inspector path/loader edge + tests |
| `sql-formatter-org/sql-formatter` | 2890 | silent | SQL whitespace formatter; dialect/path edges | SQL format dialect/path edge + tests |
| `webpack/postcss-loader` | 2842 | silent | Official webpack PostCSS loader; config/path edges | postcss-loader config/path edge + tests |
| `webpack/webpack-cli` | 2616 | silent | Webpack CLI product; config/path/command edges | webpack-cli config/path edge + tests |
| `lydell/eslint-plugin-simple-import-sort` | 2455 | silent | ESLint import-sort plugin; autofix/path edges | import-sort autofix/path edge + tests |
| `eslint-community/eslint-plugin-security` | 2375 | silent | ESLint Node security rules; rule/path edges | eslint-security rule edge + tests |
| `uiwjs/react-codemirror` | 2251 | silent | CodeMirror 6 React component; extension/path edges | CodeMirror6 extension/path edge + tests |
| `nestjs/nest-cli` | 2197 | silent | NestJS application CLI; schematic/path edges | nest-cli schematic/path edge + tests |
| `marp-team/marp-vscode` | 2088 | silent | Marp markdown slides VS Code ext; parse/path edges | Marp parse/path edge + extension tests |
| `jupyter-lsp/jupyterlab-lsp` | 2001 | silent | JupyterLab LSP integration; server/path edges | jupyterlab-lsp server/path edge + tests |
| `TypeStrong/fork-ts-checker-webpack-plugin` | 1999 | silent | Webpack TS typecheck plugin; config/path edges | fork-ts-checker config/path edge + tests |
| `eslint-stylistic/eslint-stylistic` | 1990 | silent | ESLint stylistic rules monorepo; rule/format edges | stylistic rule/format edge + tests |
| `vue-macros/vue-macros` | 1984 | silent | Vue macros/syntax-sugar toolkit; transform/path edges | vue-macros transform/path edge + tests |
| `microsoft/vscode-js-debug` | 1971 | silent | VS Code JS DAP debugger; breakpoint/path edges | js-debug breakpoint/path edge + tests |
| `webpack/minimizer-webpack-plugin` | 1966 | silent | Webpack minimizer plugin; option/path edges | minimizer option/path edge + tests |
| `microsoft/vscode-eslint` | 1952 | silent | Official ESLint VS Code extension; diagnostic/path edges | vscode-eslint diagnostic/path edge + tests |
| `callstack/repack` | 1931 | silent | RN webpack bundler toolkit; config/path edges | repack config/path edge + tests |
| `kentcdodds/mdx-bundler` | 1901 | silent | MDX/TSX string bundler; compile/path edges | mdx-bundler compile/path edge + tests |
| `microsoft/vscode-languageserver-node` | 1786 | silent | LSP node implementation libraries; protocol/path edges | lsp-node protocol/path edge + tests |
| `angular-eslint/angular-eslint` | 1783 | silent | Angular ESLint tooling monorepo; rule/path edges | angular-eslint rule/path edge + tests |
| `mtxr/vscode-sqltools` | 1765 | silent | VS Code SQL tools extension; connection/query edges | sqltools connection/query edge + tests |
| `microsoft/rnx-kit` | 1733 | silent | RN DevEx toolkit monorepo; metro/path edges | rnx-kit metro/path edge + tests |
| `serverless-heaven/serverless-webpack` | 1729 | silent | Serverless Framework webpack plugin; bundle/path edges | serverless-webpack bundle/path edge + tests |
| `microsoft/TypeScript-Sublime-Plugin` | 1702 | silent | TS language service for Sublime; protocol/path edges | sublime-ts protocol/path edge + tests |
| `microsoft/vscode-cmake-tools` | 1685 | silent | VS Code CMake Tools; configure/path edges | cmake-tools configure/path edge + tests |
| `streetsidesoftware/vscode-spell-checker` | 1679 | silent | VS Code spell checker; dictionary/path edges | spell-checker dictionary/path edge + tests |
| `sapegin/mrm` | 1646 | silent | Project-config codemods CLI; task/path edges | mrm task/path edge + tests |
| `esm-dev/modern-monaco` | 1605 | silent | Modern Monaco editor packaging; worker/path edges | modern-monaco worker/path edge + tests |
| `statoscope/statoscope` | 1581 | silent | Webpack bundle analyze/validate toolkit; report/path edges | statoscope report/path edge + tests |
| `privatenumber/pkgroll` | 1563 | silent | Zero-config Node/TS package bundler; export/path edges | pkgroll export/path edge + tests |
| `kahole/edamagit` | 1539 | silent | Magit-like Git UI for VS Code; command/path edges | edamagit command/path edge + tests |
| `qmhc/unplugin-dts` | 1526 | silent | DTS generation unplugin; emit/path edges | unplugin-dts emit/path edge + tests |
| `ducktors/turborepo-remote-cache` | 1483 | silent | Turborepo remote cache server; cache/path edges | turbo-cache path edge + tests |
| `prettier/plugin-ruby` | 1482 | silent | Prettier Ruby plugin; parse/format edges | prettier-ruby parse/format edge + tests |
| `nrwl/nx-console` | 1414 | silent | Nx/Lerna VS Code/UI console; project/path edges | nx-console project/path edge + tests |
| `chanhx/crabviz` | 1413 | silent | Interactive call-graph generator; LSP/path edges | crabviz call-graph/path edge + tests |
| `mrmckeb/typescript-plugin-css-modules` | 1393 | silent | TS LS plugin for CSS modules; completion/path edges | css-modules LS completion/path edge + tests |
| `Tencent/feflow` | 1385 | silent | Front-end engineer workflow CLI; command/path edges | feflow command/path edge + tests |
| `eslint/config-inspector` | 1383 | silent | ESLint config visual inspector; config/path edges | config-inspector path edge + tests |
| `wix/import-cost` | 1383 | silent | VS Code import-size display; package/path edges | import-cost package/path edge + tests |
| `editorconfig/editorconfig-vscode` | 1370 | silent | EditorConfig VS Code extension; property/path edges | editorconfig property/path edge + tests |
| `TypeFox/monaco-languageclient` | 1366 | silent | Monaco language-client toolbox; LSP/path edges | monaco-languageclient LSP/path edge + tests |
| `fannheyward/coc-pyright` | 1361 | silent | coc.nvim Pyright extension; LSP/path edges | coc-pyright LSP/path edge + tests |
| `folke/ultra-runner` | 1247 | silent | Fast monorepo script runner; workspace/path edges | ultra-runner workspace/path edge + tests |
| `simonhaenisch/prettier-plugin-organize-imports` | 1239 | silent | Prettier organize-imports via TS LS; sort/path edges | organize-imports sort/path edge + tests |
| `fi3ework/vite-plugin-checker` | 1239 | silent | Vite checker plugin (TS/ESLint/Stylelint); overlay/path edges | vite-plugin-checker overlay/path edge + tests |
| `gajus/eslint-plugin-jsdoc` | 1229 | silent | ESLint JSDoc rules; tag/path edges | jsdoc rule/tag edge + tests |
| `jest-community/eslint-plugin-jest` | 1170 | silent | ESLint Jest plugin; rule/path edges | eslint-jest rule edge + tests |
| `just-jeb/angular-builders` | 1162 | silent | Angular builders (Jest/custom webpack); builder/path edges | angular-builders builder/path edge + tests |
| `fannheyward/coc-rust-analyzer` | 1156 | silent | coc.nvim rust-analyzer extension; LSP/path edges | coc-rust-analyzer LSP/path edge + tests |
| `weirongxu/coc-explorer` | 1148 | silent | coc.nvim file explorer; tree/path edges | coc-explorer tree/path edge + tests |
| `istanbuljs/istanbuljs` | 1103 | silent | Istanbul coverage tooling monorepo; instrument/path edges | istanbul instrument/path edge + tests |
| `yioneko/vtsls` | 1092 | silent | VS Code TS extension as LSP wrapper; protocol/path edges | vtsls protocol/path edge + tests |
| `neoclide/coc-tsserver` | 1080 | silent | coc.nvim tsserver extension; completion/path edges | coc-tsserver completion/path edge + tests |
| `testing-library/eslint-plugin-testing-library` | 1063 | silent | Testing Library ESLint plugin; rule/path edges | testing-library-eslint rule edge + tests |
| `eclipse-langium/langium` | 1035 | silent | Langium DSL/language-engineering framework; grammar/LSP edges | langium grammar/LSP edge + tests |
| `web-infra-dev/rslib` | 1032 | silent | Rsbuild library bundler; config/path edges | rslib config/path edge + tests |
| `eslint-community/eslint-plugin-promise` | 1003 | silent | ESLint promise best-practice rules; rule/path edges | eslint-promise rule edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `callstack/haul` | 3677 | silent | Superseded RN bundler — prefer callstack/repack |
| `json-schema-faker/json-schema-faker` | 3448 | silent | Fake-data generator from schema — prefer schema lint/codegen product homes |
| `nuxt/devtools` | 3298 | agentscan | AgentScan adopter org (nuxt) — leave circle |
| `unjs/unbuild` | 2727 | agentscan | AgentScan adopter org (unjs) — leave circle |
| `mzgoddard/hard-source-webpack-plugin` | 2724 | silent | Stale webpack cache plugin (quiet years) — prefer active webpack/rspack homes |
| `unjs/magicast` | 2477 | agentscan | AgentScan adopter org (unjs) — leave circle |
| `godotengine/godot-vscode-plugin` | 2123 | silent | Godot agent-ban circle — leave vscode plugin with engine |
| `zenbu-labs/terminal-code` | 1982 | silent | Terminal VS Code novelty — weak DevEx product hunk class vs LSP/formatter farms |
| `rohitdhas/shittier` | 1804 | silent | Novelty joke formatter — not playbook farm hunk class |
| `electron/devtron` | 1775 | silent | Quiet Electron DevTools extension — prefer active Electron/devtools homes |
| `jonschlinkert/markdown-toc` | 1754 | silent | Quiet markdown TOC utility — thin CLI, prefer active MDX/remark homes |
| `privatenumber/minification-benchmarks` | 1620 | silent | Benchmark suite not product CLI/LSP/formatter home |
| `antfu/esno` | 1604 | silent | Thin tsx alias package — prefer privatenumber/tsx product |
| `ChromeDevTools/devtools-protocol` | 1545 | silent | Protocol type definitions — specs-only, weak contribution farm |
| `apollographql/apollo-client-devtools` | 1528 | silent | Browser DevTools panel for Apollo Client — app-devtools UI, weak playbook hunk |
| `Redocly/redocly-cli` | 1510 | hard_ban | NO-AI / AGENTS.md ban — hard leave |
| `stylelint/stylelint-config-standard` | 1419 | silent | Shareable config only — prefer stylelint core/plugin product |
| `egoist/import-http` | 1234 | silent | Quiet URL-import experiment — prefer active bundler plugin homes |
| `vitejs/devtools` | 1192 | agentscan | AgentScan adopter org (vitejs) — leave circle |
| `egoist/bili` | 1030 | silent | Quiet/legacy JS bundler — prefer pkgroll/tsup/rslib homes |

Notes: Prefer midband TS/JS DevEx product homes from the 1k–2k universe fill + 1k–5k midband (LSP/coc/vtsls/langium/monaco-languageclient, ESLint/Prettier/Stylelint/sql-formatter/spectral, webpack/rollup/pkgroll/rslib/repack loaders+CLIs, Monaco/CodeMirror/Remirror/VS Code extensions, codemod/mrm/vue-macros, knip-adjacent CLI/schema/source-map). Leave AgentScan (nuxt/unjs/vitejs), Redocly NO-AI, Godot circle, superseded haul/esno/bili/hard-source, novelty shittier/terminal-code, specs-only devtools-protocol, thin configs/benchmarks/aliases.

