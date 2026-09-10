# Sector survey: editors-devex

Account: `vulragrag-star` · refreshed `2026-09-08T17:38:01Z` · TS/JS/Zig DevEx slice · No fork/PR/comment.

Playbook lens: parser/path/formatter/LSP/bundler tooling with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 100 | No hard ban in common paths |
| disclosure | 4 | AI disclosure language |
| hard_ban | 1 | Hard AI ban |
| agentscan | 2 | AgentScan |
| hostility_risk | 1 | Hostility-adjacent |

Proceed: **69** · Leave: **39**.

## PROCEED candidates (contrib fit)

| Repo | Stars | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `neovim/neovim` | 102213 | disclosure | AGENTS.md AI-assisted trailer; famous terminal editor + LSP host | path/option/Lua runtime edge + tests |
| `zed-industries/zed` | 89921 | disclosure | soft CONTRIBUTING disclosure; human judgement; max 3 open PRs | path/project-open or config parse + tests |
| `coder/code-server` | 79236 | silent | VS Code in browser; no hard AI ban | path/proxy/config edge + tests |
| `mozilla/pdf.js` | 53846 | silent | PDF parser surface with unit-test culture; product code home | parser edge + unit tests |
| `prettier/prettier` | 52240 | silent | Opinionated formatter with strong fixture tests | parser/printer fixture edge + tests |
| `parcel-bundler/parcel` | 44024 | silent | Zero-config web bundler; resolve/path/config edges | bundle resolve/path/config edge + tests |
| `typicode/husky` | 35309 | silent | Git hooks manager; hook path/config edges | hook path/config edge + tests |
| `postcss/postcss` | 28974 | silent | CSS transform engine; plugin/parse/path edges | CSS plugin/parse/path edge + tests |
| `eslint/eslint` | 27499 | silent | Famous JS linter product; rule/AST/path fixture culture | lint rule/AST/path edge + tests |
| `rollup/rollup` | 26309 | silent | ESM bundler; plugin/resolve/path edges | bundle resolve/path/plugin edge + tests |
| `conventional-changelog/commitlint` | 18735 | silent | Commit message linter; rule/config edges | commitlint rule/config edge + tests |
| `git-lfs/git-lfs` | 14476 | silent | Git LFS; path/transfer edges | pointer/path/transfer edge + tests |
| `coder/coder` | 14399 | silent | Cloud IDE / workspace product; no hard ban for human-owned fixes | CLI flag/path/template edge + tests |
| `rolldown/rolldown` | 13943 | silent | Rust Rollup-compatible bundler; resolve/path edges | bundle resolve/path edge + tests |
| `jonas/tig` | 13327 | silent | Classic text-mode git UI; parse/path surface | argv/path/config edge + tests |
| `TypeStrong/ts-node` | 13128 | silent | TypeScript execute/REPL; loader/path/config edges | TS loader/path/config edge + tests |
| `privatenumber/tsx` | 12136 | silent | Fast TypeScript execute; loader/path edges | TS execute/loader/path edge + tests |
| `stylelint/stylelint` | 11518 | silent | CSS linter product; rule/config/path edges | CSS lint rule/config edge + tests |
| `egoist/tsup` | 11293 | silent | TypeScript library bundler; config/entry/path edges | bundle entry/path/config edge + tests |
| `mawww/kakoune` | 11049 | silent | Terminal editor; copyright-waiver empty commit; no AI ban | command/parser quoting edge + tests |
| `a-h/templ` | 10532 | silent | Go HTML templ + LSP; discuss before large PRs | template parser/escape edge + tests |
| `facebook/jscodeshift` | 10041 | silent | JS codemod toolkit; transform/AST/path edges | codemod AST/path edge + tests |
| `AGWA/git-crypt` | 9895 | silent | Transparent git encryption; small C++ surface | filter path/smudge edge + tests |
| `terser/terser` | 9330 | silent | JS parser/mangler/compressor; AST/fixture edges | JS AST minify/parse edge + tests |
| `evilmartians/lefthook` | 8786 | silent | Git hooks manager; config/path/glob edges | hook path/glob/config edge + tests |
| `TypeStrong/typedoc` | 8453 | silent | TypeScript API docs generator; reflect/path edges | TS reflect/path/doc edge + tests |
| `j178/prek` | 8382 | silent | Rust pre-commit alternative; hook config edges | config/path edge + tests |
| `xojs/xo` | 7991 | silent | Opinionated ESLint wrapper CLI; config/path edges | lint config/path edge + tests |
| `bensadeh/tailspin` | 7959 | silent | Terminal log highlighter; small Rust CLI | regex/theme/path config edge + tests |
| `rust-lang/rustfmt` | 6961 | silent | Rust formatter; usable with correctness bar | config/edition/path edge + tests |
| `facebook/pyrefly` | 6946 | silent | Python LSP/typechecker; claim issues first; Meta CLA | config/path/parse edge + tests |
| `dominikh/go-tools` | 6890 | silent | Staticcheck / go-tools analyzer product | analyzer/pattern edge + tests |
| `tummychow/git-absorb` | 5715 | silent | git commit --fixup automation; small Rust CLI | path/commit selection edge + tests |
| `zigtools/zls` | 5116 | silent | Zig language server; LSP/parse/path - not ziglang/zig | Zig LSP/parse/path edge + tests |
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
| `github/gitignore` | 175660 | silent | template dump not product |
| `airbnb/javascript` | 148182 | silent | style-guide docs farm |
| `excalidraw/excalidraw` | 131388 | silent | whiteboard UI-heavy |
| `microsoft/playwright` | 95802 | disclosure | Browser test mega-framework - prefer lint/format/LSP homes |
| `puppeteer/puppeteer` | 95566 | silent | Browser automation - weak parser/formatter hunk fit |
| `toeverything/AFFiNE` | 72315 | silent | Notion-like UI farm |
| `withastro/astro` | 62394 | agentscan | AgentScan adopter org |
| `upstash/context7` | 61763 | silent | docs-context farm risk |
| `nuxt/nuxt` | 60830 | agentscan | AgentScan adopter org |
| `adam-p/markdown-here` | 60247 | silent | stale extension / weak fit |
| `ChromeDevTools/chrome-devtools-mcp` | 51318 | silent | MCP satellite |
| `cypress-io/cypress` | 51034 | silent | prefer lint/format homes first |
| `microsoft/monaco-editor` | 46692 | silent | Browser editor UI-heavy - prefer LSP/formatter homes |
| `jestjs/jest` | 45480 | silent | Test runner mega - prefer eslint/stylelint/formatters |
| `fish-shell/fish-shell` | 34151 | hard_ban | generative AI ban in CONTRIBUTING.rst |
| `standard/standard` | 29427 | silent | Style-guide + fixer - prefer eslint cores |
| `ajaxorg/ace` | 27146 | silent | Browser editor UI - weak systems hunk fit |
| `avajs/ava` | 20827 | silent | Node test runner - not DevEx parser/LSP core |
| `xi-editor/xi-editor` | 19819 | silent | low-maintenance research editor |
| `vnotex/vnote` | 12936 | silent | note app farm risk |
| `mapeditor/tiled` | 12874 | silent | game map editor wrong class |
| `antirez/kilo` | 9112 | silent | teaching editor not product target |
| `LibreSprite/LibreSprite` | 8359 | silent | niche fork |
| `kunchenguid/no-mistakes` | 8350 | silent | not famous systems product core |
| `Sigil-Ebook/Sigil` | 6948 | silent | ebook editor wrong class |
| `LongSoft/UEFITool` | 5660 | silent | niche firmware tool |
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

## Famous editors/shells score pass (2026-09-10, +23 scored · editors-devex)

Account: `vulragrag-star` · Famous shells/editors atlas slice (tmux/helix/lapce/kitty/wezterm + adjacent mux/editor/TUI homes) · Policy via `raw.githubusercontent.com` + manual AI_POLICY reads · **17** proceed / **6** leave in this sector subset · Bands: &lt;1k through 20k+ · No fork/PR/comment.

Policy histogram (this sector subset): `{'silent': 20, 'disclosure': 3}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `helix-editor/helix` | 46159 | silent | Post-modern modal terminal editor; config/LSP/grammar/path edges | config/LSP/path edge + Rust tests |
| `charmbracelet/bubbletea` | 44874 | silent | Go TUI framework (DevEx); model/update/cmd message edges | Elm-arch msg/cmd edge + Go tests |
| `lapce/lapce` | 38833 | silent | Rust code editor; config/plugin/path/LSP edges | config/plugin/path edge + Rust tests |
| `micro-editor/micro` | 29555 | silent | Modern terminal text editor; config/plugin/path/keybind edges | config/plugin/path edge + Go tests |
| `neoclide/coc.nvim` | 25164 | silent | Vim/Neovim LSP extension host; config/path/language-server edges | LSP/config/path edge + TS/Vim tests |
| `ratatui/ratatui` | 22540 | disclosure | Rust TUI framework; layout/backend/widget edges (disclose AI use; human-owned PRs) | layout/widget/backend edge + Rust tests — disclose AI |
| `nvim-telescope/telescope.nvim` | 19779 | silent | Neovim fuzzy finder; path/picker/preview edges | picker/path/preview edge + Lua tests |
| `rivo/tview` | 14091 | silent | Go TUI widgets; form/table/focus navigation edges | widget/focus/form edge + Go tests |
| `charmbracelet/lipgloss` | 11807 | silent | Terminal style/layout library; width/ANSI/wrap edges | style/wrap/ANSI edge + Go tests |
| `prompt-toolkit/python-prompt-toolkit` | 10565 | silent | Python prompt toolkit; completion/keybind/path edges | completion/keybind edge + Python tests |
| `saulpw/visidata` | 9267 | disclosure | Terminal data spreadsheet; loader/path/type edges (human gate for AI-assisted code) | loader/path/type edge + Python tests — human-review AI |
| `charmbracelet/bubbles` | 8892 | silent | Bubble Tea component kit; input/list/viewport edge cases | component input/list edge + Go tests |
| `vscode-neovim/vscode-neovim` | 7732 | silent | VS Code Neovim bridge; path/RPC/mode edges | RPC/path/mode edge + TS tests |
| `charmbracelet/huh` | 7158 | silent | Terminal forms library; validation/prompt/path edges | form/validate/prompt edge + Go tests |
| `slap-editor/slap` | 6188 | silent | Sublime-like terminal editor; path/config edges | editor path/config edge + JS tests |
| `gyscos/cursive` | 4846 | silent | Rust TUI library; focus/layout/event edges | focus/layout/event edge + Rust tests |
| `urwid/urwid` | 3017 | silent | Python console UI library; widget/layout edges | widget/layout edge + Python tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `microsoft/vscode` | 191536 | silent | Enormous IDE megaproject — mentor-heavy; prefer LSP/formatter/editor-core homes |
| `Aider-AI/aider` | 48867 | silent | AI pair-programming agent product — agent surface, not editor/shell atlas class |
| `Textualize/textual` | 37186 | disclosure | AI_POLICY: AI PRs only after maintainer-approved issue + disclose agent — framework gate like rich; leave |
| `VSCodium/vscodium` | 33179 | silent | Binary packaging/telemetry-strip of VS Code — not primary product source home |
| `charmbracelet/crush` | 27981 | silent | Agentic coding assistant product — not classic editor/mux/CLI hunk farm |
| `neovide/neovide` | 15207 | silent | GUI Neovim frontend — heavy GUI surface; prefer terminal editor/LSP homes |

Notes: Prefer terminal editors (helix/lapce/micro) and DevEx TUI libs (bubbletea/ratatui/tview) with config/path/LSP edges. Disclosure homes (ratatui/visidata) need human-owned PR bodies. Leave vscode megaproject, VSCodium packaging, neovide GUI, crush/aider agent products, textual (maintainer-approved AI issue gate like rich).

