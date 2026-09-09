# Sector survey: cli-systems (mid-band 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/cli-systems-midband.jsonl` (~5338 noisy) · Deep-sampled **100** real CLI/sys products via `gh api` contents (CONTRIBUTING/AI_POLICY/AGENTS/PR templates) · Hard leaves + predecessor queues respected · No fork/PR/comment.

Playbook lens: famous-ish **main product** (1k–5k★), not AgentScan, not hard AI ban, hunk class = **CLI argv / path / quoting / config-parser / shell-integration bugs with regression tests** (fselect/gojq/sad/choose/xplr/util-linux class — not games/emulators, not AI-agent farms, not awesome/tutorials, not library-only).

## Policy histogram (deep sample of 100)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 94 | Most mid-band classic CLIs still have no hard AI ban page |
| disclosure | 6 | diffnav, qsv, strace, labwc, u-root, rizin, … |
| hostility_risk | 0 | — |
| hard_ban | 0 | none after review (rizin/lxd false positives corrected) |
| agentscan | 0 | None in this sample |

Proceed: **90** · Leave: **10** · Scored lines appended to `survey/scored.jsonl` with `"band":"1k-5k"`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class (CLI path/quoting/parser + tests). Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork. **Do not steal** predecessor open queues (`denoland/deno`, `go-gitea/gitea`, `apache/nuttx`, `tianocore/edk2`, `mesonbuild/meson`, `pypa/hatch`).

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `tfutils/tfenv` | 4967 | silent | Terraform version manager; path/shim | version path/shim edge + shell tests |
| `charmbracelet/freeze` | 4825 | silent | terminal screenshot CLI; path/argv | path/argv edge + Go tests |
| `canonical/lxd` | 4825 | silent | system container/VM manager CLI; path/config (Copilot-instructions ≠ AI ban) | instance/path config edge + Go tests |
| `sayanarijit/xplr` | 4816 | silent | TUI file explorer; path/config/lua plugin edges | path/config/lua plugin edge + Rust tests |
| `koute/bytehound` | 4809 | silent | memory profiler CLI; path/trace | trace path edge + Rust tests |
| `yshui/picom` | 4792 | silent | X11 compositor; config/path parser (checkbox false-positive fixed) | config path/parser edge + C tests |
| `tmux-python/tmuxp` | 4572 | silent | tmux session manager; YAML/path | session YAML/path edge + Python tests |
| `mr-karan/doggo` | 4467 | silent | DNS client CLI; query/argv | DNS query/argv edge + Go tests |
| `jhspetersson/fselect` | 4458 | silent | SQL-like find CLI; path/query parser | path/query parse edge + Rust tests |
| `dvorka/hstr` | 4455 | silent | shell history TUI; argv/history path | history path / argv edge + C tests |
| `orhun/binsider` | 4418 | silent | ELF binary analyzer TUI; path/ELF parse | ELF/path parse edge + Rust tests |
| `mstange/samply` | 4410 | silent | sampling profiler CLI; path/symbolicate | path/symbolicate edge + Rust tests |
| `NixOS/patchelf` | 4258 | silent | ELF RPATH rewriter; path/ELF | ELF/path edge + C++ tests |
| `hackerb9/lsix` | 4175 | silent | ls for sixel images; path/glob | path/glob edge + shell tests |
| `KDE/heaptrack` | 4158 | silent | heap profiler CLI; path/trace | trace path edge + C++ tests |
| `version-fox/vfox` | 3979 | silent | cross-platform version manager; path/plugin | plugin path / shim edge + Go tests |
| `Adembc/lazyssh` | 3921 | silent | SSH manager TUI; config/path/host | SSH config/path edge + Go tests |
| `rizinorg/rizin` | 3873 | disclosure | disclosure required; no AI on good-first-issue; unverified AI closed; RE CLI path/format | binary path/format edge + C tests — disclose AI; avoid GFI |
| `MisterTea/EternalTerminal` | 3873 | silent | re-connectable remote shell; path/argv | ssh/path edge + C++ tests |
| `itchyny/gojq` | 3799 | silent | jq clone in Go; expression/path parser | expr/path parse edge + Go tests |
| `dathere/qsv` | 3776 | disclosure | disclosure required; CSV wrangling CLI; path/schema | CSV path/schema edge + Rust tests |
| `DarthSim/overmind` | 3740 | silent | Procfile process manager; path/tmux | Procfile/path edge + Go tests |
| `kamiyaa/joshuto` | 3723 | silent | ranger-like file manager; path/config | path/config edge + Rust tests |
| `rs/curlie` | 3716 | silent | curl+httpie CLI; argv/header quoting | argv/header quoting edge + Go tests |
| `raboof/nethogs` | 3691 | silent | per-process net top; path/proc | proc/net path edge + C++ tests |
| `str4d/rage` | 3646 | silent | age encryption CLI; path/recipient parse | path/recipient parse edge + Rust tests |
| `antonmedv/walk` | 3639 | silent | terminal file manager; path/preview | path/preview edge + Go tests |
| `cespare/reflex` | 3551 | silent | file-watch command runner; path/glob | path/glob edge + Go tests |
| `containers/toolbox` | 3490 | silent | container CLI env; path/image | image/path edge + Go tests |
| `moncho/dry` | 3275 | silent | Docker TUI; container ref/path | container ref/path edge + Go tests |
| `atanunq/viu` | 3272 | silent | terminal image viewer; path/format | image path/format edge + Rust tests |
| `vifm/vifm` | 3263 | silent | curses file manager; path/command parser | path/cmd parse edge + C tests |
| `emersion/mako` | 3250 | silent | Wayland notification daemon; config/path | config path / dbus edge + C tests |
| `rustic-rs/rustic` | 3236 | silent | restic-compatible backup CLI; path/repo | repo path/quoting edge + Rust tests |
| `util-linux/util-linux` | 3226 | silent | classic Linux utilities; path/quoting/parser | path/quoting/parser edge + C tests |
| `landley/toybox` | 3146 | silent | BusyBox-like multicall; argv/path | argv/path edge + C tests |
| `imsnif/diskonaut` | 3126 | silent | disk space TUI; path/mount | path/mount edge + Rust tests |
| `u-root/u-root` | 3071 | disclosure | disclosure required; Go userland/bootloaders; path/cmd | cmd/path edge + Go tests |
| `bvaisvil/zenith` | 3049 | silent | htop-like system monitor; path/proc | proc/path edge + Rust tests |
| `leftwm/leftwm` | 3047 | silent | tiling WM; config/path | config path edge + Rust tests |
| `orhun/kmon` | 2945 | silent | kernel module TUI; path/modinfo | module path edge + Rust tests |
| `voidint/g` | 2876 | silent | Go version manager; path/shim | GOROOT path/shim edge + Go tests |
| `Canop/dysk` | 2853 | silent | df-like filesystem CLI; path/mount | mount/path edge + Rust tests |
| `labwc/labwc` | 2770 | disclosure | disclosure required; Wayland stacking compositor; config/path | config path edge + C tests |
| `F1bonacc1/process-compose` | 2757 | silent | Procfile/process orchestrator; path/yaml | compose path/yaml edge + Go tests |
| `hzeller/timg` | 2749 | silent | terminal image/video viewer; path/format | image path/format edge + C++ tests |
| `okbob/pspg` | 2730 | silent | unix pager for tables; path/argv | pager path/argv edge + C tests |
| `jorgebucaran/nvm.fish` | 2712 | silent | Fish node version manager; path/quoting | NODE path/quoting + fish tests |
| `jfernandez/bpftop` | 2702 | silent | eBPF top TUI; path/prog id | prog id/path edge + Rust tests |
| `strace/strace` | 2692 | disclosure | disclosure required; syscall tracer; path/argv | path/argv edge + C tests |
| `solidiquis/erdtree` | 2598 | silent | tree/du CLI; path/ignore | path/ignore edge + Rust tests |
| `mag37/dockcheck` | 2501 | silent | docker image update CLI; path/compose | compose/path edge + shell tests |
| `sahib/rmlint` | 2421 | silent | duplicate finder CLI; path/hash | path/hash edge + C tests |
| `afnanenayet/diffsitter` | 2397 | silent | AST diff CLI; path/lang | path/lang edge + Rust tests |
| `ifd3f/caligula` | 2301 | silent | disk imaging TUI; path/device (checkbox false-positive fixed) | device/path edge + Rust tests |
| `theryangeary/choose` | 2270 | silent | cut/awk alternative CLI; field/parse | field/parse edge + Rust tests |
| `sharkdp/vivid` | 2259 | silent | LS_COLORS theme CLI; path/config | theme/path edge + Rust tests |
| `elfmz/far2l` | 2210 | silent | FAR file manager Linux port; path/cmd | path/cmd edge + C++ tests |
| `alexhallam/tv` | 2166 | silent | CSV pretty-printer CLI; path/format | CSV path/format edge + Rust tests |
| `kdheepak/taskwarrior-tui` | 2120 | silent | taskwarrior TUI; path/filter | filter/path edge + Rust tests |
| `EFForg/apkeep` | 2049 | silent | APK download CLI; path/source | APK path/source edge + Rust tests |
| `ms-jpq/sad` | 2046 | silent | CLI search-replace; path/regex | path/regex edge + Rust tests |
| `unkn0wn-root/resterm` | 1914 | silent | HTTP/gRPC API client TUI; path/.http | .http path/parse edge + Go tests |
| `homeport/dyff` | 1882 | silent | YAML/JSON diff CLI; path/doc | YAML path/diff edge + Go tests |
| `linux-nvme/nvme-cli` | 1863 | silent | NVMe management CLI; optional AI companion repo only — no disclosure mandate | device path/arg edge + C tests |
| `cupcakearmy/autorestic` | 1861 | silent | restic backup CLI wrapper; path/config | config path/backend edge + Go tests |
| `aquaproj/aqua` | 1840 | silent | declarative CLI version manager; path/registry | registry path/shim edge + Go tests |
| `google/yamlfmt` | 1823 | silent | YAML formatter CLI; path/config | path/config edge + Go tests |
| `orhun/gpg-tui` | 1759 | silent | GnuPG TUI; key/path | keyring path edge + Rust tests |
| `nivekuil/rip` | 1733 | silent | safe rm alternative; path/graveyard | path/graveyard edge + Rust tests |
| `leo-arch/clifm` | 1722 | silent | CLI file manager; path/cmd parser | path/cmd parse edge + C tests |
| `project-copacetic/copacetic` | 1703 | silent | container image patch CLI; path/ref | image ref/path edge + Go tests |
| `yamafaktory/jql` | 1675 | silent | JSON query CLI; path/expr | JSON path/expr edge + Rust tests |
| `kimono-koans/httm` | 1658 | silent | ZFS/btrfs time-machine CLI; path/snap | snapshot path edge + Rust tests |
| `pacstall/pacstall` | 1655 | silent | Ubuntu AUR-like pkg manager; path/script | pacscript path edge + shell tests |
| `GothenburgBitFactory/timewarrior` | 1654 | silent | time tracking CLI; path/db | db/path edge + C++ tests |
| `quantumsheep/sshs` | 1596 | silent | SSH TUI; config/path | SSH config/path edge + Go tests |
| `dlvhdr/diffnav` | 1555 | disclosure | disclosure required; git diff pager TUI; path/delta | diff path/tree edge + Go tests |
| `dimonomid/nerdlog` | 1555 | silent | multi-host log TUI; path/ssh | log path/ssh edge + Go tests |
| `mike-engel/jwt-cli` | 1511 | silent | JWT encode/decode CLI; argv/path | token/argv edge + Rust tests |
| `orhun/systeroid` | 1468 | silent | sysctl TUI; path/param | sysctl path/param edge + Rust tests |
| `tofuutils/tenv` | 1433 | silent | OpenTofu/TF version manager; path/shim | version path/shim edge + Go tests |
| `bluetuith-org/bluetuith` | 1401 | silent | bluetooth TUI; device/path | device/config edge + Go tests |
| `ivan-hc/AM` | 1358 | silent | AppImage package manager; path/script | AppImage path/script edge + shell tests |
| `coastalwhite/lemurs` | 1356 | silent | TUI login manager; path/session | session/path edge + Rust tests |
| `abhimanyu003/sttr` | 1348 | silent | string transform CLI; argv/pipe | argv/pipe edge + Go tests |
| `lavv17/lftp` | 1300 | silent | file transfer CLI; URL/path/quoting | URL/path quoting edge + C++ tests |
| `SoptikHa2/desed` | 1218 | silent | sed debugger CLI; path/script | sed script/path edge + Rust tests |
| `irontec/sngrep` | 1203 | silent | SIP message flow TUI; pcap/path | pcap/path edge + C tests |
| `filiparag/wikiman` | 1015 | silent | offline docs search CLI; path/db | doc path/db edge + shell tests |

### Tier notes — best first homes (mid-band)

1. `jhspetersson/fselect` — silent; SQL-like find; path/query parser + Rust tests.
2. `itchyny/gojq` — silent; jq clone; expression/path parser + Go tests.
3. `ms-jpq/sad` — silent; Space Age seD; path/regex + Rust tests.
4. `theryangeary/choose` — silent; cut/awk alternative; field parse + Rust tests.
5. `sayanarijit/xplr` / `kamiyaa/joshuto` / `antonmedv/walk` / `vifm/vifm` — TUI file managers; path/config.
6. `util-linux/util-linux` — silent (AGENTS: human-only commit credit; Signed-off-by); classic path/quoting/parser.
7. `strace/strace` — disclosure culture / AI must not be co-author; syscall path/argv + C tests.
8. `rs/curlie` / `mr-karan/doggo` / `dathere/qsv` — HTTP/DNS/CSV CLIs; argv/path/schema (qsv: disclose AI).
9. `NixOS/patchelf` / `landley/toybox` / `solidiquis/erdtree` / `Canop/dysk` / `nivekuil/rip` — ELF/coreutils-adjacent path edges.
10. `rustic-rs/rustic` / `cupcakearmy/autorestic` / `str4d/rage` — backup/encryption path/repo edges.
11. `homeport/dyff` / `google/yamlfmt` / `dlvhdr/diffnav` — YAML/diff path edges (diffnav: AI_POLICY disclose).
12. `cespare/reflex` / `F1bonacc1/process-compose` / `DarthSim/overmind` — watch/orchestrator path/YAML.

## LEAVE table

| Repo | ★ | Policy | Why leave |
|---|---:|---|---|
| `Aloxaf/fzf-tab` | 4922 | silent | zsh completion plugin — not standalone CLI product |
| `liquidprompt/liquidprompt` | 4675 | silent | shell prompt framework — thin product vs classic CLI utilities |
| `plasma-umass/coz` | 4543 | silent | causal profiler with built-in LLM agent features — AI-adjacent product surface |
| `IlanCosman/tide` | 4260 | silent | Fish prompt theme — not a standalone CLI/sys product for path/quoting hunks |
| `charmbracelet/pop` | 2906 | silent | email-from-terminal — weak path/quoting/parser hunk class |
| `bpkg/bpkg` | 1974 | silent | bash package manager scaffolding — thin vs famous CLI utilities |
| `charmbracelet/skate` | 1830 | silent | personal KV store — weak CLI path/quoting hunk class |
| `charmbracelet/wishlist` | 1661 | silent | SSH directory TUI — thin vs core CLI/sys utilities |
| `basherpm/basher` | 1302 | silent | shell-script package manager — thin vs famous CLI utilities |
| `getsentry/sentry-cli` | 1039 | silent | Sentry SaaS ops CLI — lower path/quoting product fit for this sector |

## Hard leaves respected (not sampled / auto-excluded)

Cython, OpenJDK, Zig LLM ban, SQLite agentic, Godot, Gentoo, QEMU AI, AgentScan circle, alacritty/yt-dlp/ghostty/SDL patterns, predecessor queues (deno/gitea/nuttx/edk2/meson/hatch/…), satellites (`pypa/distutils` etc.), games/emulators/AI-agent farms/awesome/tutorials/libraries filtered from the ~5k noisy shard.

## Notes

Per-repo policy fetch artifacts: `survey/notes/cli-systems-midband-raw/*.json`  
Curated scored copy: `survey/notes/cli-systems-midband-scored.jsonl`

## Deepen pass (2026-09-09, +49 scored)

Account: `vulragrag-star` · Curated product midband leftovers — upgrade/env CLIs, search/find, CSV/jq/typos, git adjacency, compress/transfer, HTTP bench, Wayland/X11 utils, shells · Policy via `raw.githubusercontent.com` · **43** proceed / **6** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 47, 'disclosure': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `rfjakob/gocryptfs` | 4601 | silent | Encrypted overlay filesystem CLI; path/mount/cipher | mount/path/cipher edge + Go tests |
| `tokio-rs/console` | 4599 | silent | Async Rust debugger/console TUI; path/tokio instrumentation | console path/target edge + Rust tests |
| `jakehilborn/displayplacer` | 4518 | silent | macOS multi-display configuration CLI; display/path | display config edge + C tests |
| `six-ddc/plow` | 4517 | silent | High-performance HTTP benchmarking CLI with realtime TUI; URL/argv | bench URL/argv edge + Go tests |
| `topgrade-rs/topgrade` | 4498 | silent | Cross-platform upgrade-all-the-things CLI; path/package manager edges | upgrade path/config edge + Rust tests |
| `medialab/xan` | 4497 | silent | CSV wrangling CLI (xsv-class); path/schema/select | CSV path/select edge + Rust tests |
| `OpenVPN/easy-rsa` | 4476 | silent | Simple shell-based CA utility; path/PKI | PKI path/script edge + shell tests |
| `vslavik/diff-pdf` | 4311 | silent | Visual PDF comparison CLI; path/page | PDF path/diff edge + C++ tests |
| `rhysd/actionlint` | 4200 | silent | Static checker for GitHub Actions workflows; path/YAML | workflow path/YAML lint edge + Go tests |
| `peak/s5cmd` | 4184 | silent | Parallel S3 and local filesystem execution tool; path/URI | S3 URI/path edge + Go tests |
| `imapsync/imapsync` | 4146 | silent | IMAP mailbox transfer CLI; host/folder/path | IMAP folder/path edge + Perl/shell tests |
| `qustavo/httplab` | 4139 | silent | Interactive web server for inspecting HTTP; path/argv | HTTP inspect/path edge + Go tests |
| `crate-ci/typos` | 4125 | silent | Source code spell checker CLI; path/config/dict | path/dict/config edge + Rust tests |
| `arxanas/git-branchless` | 4124 | silent | High-velocity git workflow tooling; path/ref/branch | git ref/branch edge + Rust tests |
| `flox/flox` | 4123 | silent | Nix-based env/package manager CLI; path/activation (CLA + signed commits) | env/path/activation edge + Rust/Nix tests — accept CLA |
| `zu1k/nali` | 4104 | silent | Offline IP geo/CDN query CLI; path/db/argv | IP db/path edge + Go tests |
| `Drewsif/PiShrink` | 4104 | silent | Shrink Raspberry Pi images CLI; path/image | image path/shrink edge + shell tests |
| `runfinch/finch` | 4059 | silent | AWS Finch container client CLI (nerdctl/lima adjacency); path/image/VM | container ref/path/VM edge + Go tests |
| `sobolevn/git-secret` | 4043 | silent | Bash tool to store private data inside a git repo; path/gpg | git-secret path/gpg edge + shell tests |
| `icholy/ttygif` | 4012 | silent | Convert terminal recordings to animated gifs; path/ttyrec | ttyrec path edge + C tests |
| `kashav/fsql` | 3987 | silent | SQL-like filesystem search CLI; path/query parser | path/query parse edge + Go tests |
| `YS-L/csvlens` | 3956 | silent | Command-line CSV viewer; path/format | CSV path/view edge + Rust tests |
| `nakabonne/ali` | 3940 | silent | HTTP load generator with realtime plots; URL/argv | load URL/argv edge + Go tests |
| `newsboat/newsboat` | 3902 | silent | Terminal RSS/Atom reader; path/url/config | feed URL/config path edge + C++ tests |
| `neomutt/neomutt` | 3828 | disclosure | disclosure required for AI assistance; mutt-class mail client; path/config | config/path/MIME edge + C tests — disclose AI |
| `ouch-org/ouch` | 3743 | silent | Painless compression/decompression CLI; path/archive format | archive path/format edge + Rust tests |
| `axel-download-accelerator/axel` | 3401 | silent | Lightweight CLI download accelerator; URL/path/argv | URL/path/argv edge + C tests |
| `jhawthorn/fzy` | 3300 | silent | Simple fast fuzzy finder for the terminal; argv/match | fuzzy match/argv edge + C tests |
| `Genivia/ugrep` | 3279 | silent | User-friendly ultra-fast file pattern searcher CLI; path/glob/regex | path/glob/regex edge + C++ tests |
| `noahgorstein/jqp` | 2835 | silent | TUI playground for jq expressions; expr/path | jq expr/TUI edge + Go tests |
| `bugaevc/wl-clipboard` | 2430 | silent | Wayland command-line copy/paste utilities; path/MIME | clipboard MIME/path edge + C tests |
| `hykilpikonna/hyfetch` | 2104 | silent | Neofetch-class system info CLI with pride flags; path/config | sysinfo config/path edge + shell/Python tests |
| `Macchina-CLI/macchina` | 1969 | silent | System information frontend CLI; path/config | sysinfo config/path edge + Rust tests |
| `gsamokovarov/jump` | 1945 | silent | Directory jumper CLI that learns habits; path/db | jump path/db edge + Go tests |
| `lmorg/murex` | 1913 | silent | Smarter shell and scripting environment; argv/path/parser | shell parse/path edge + Go tests |
| `eth-p/bat-extras` | 1627 | silent | Bash scripts integrating bat with other CLIs; path/argv | bat wrapper path edge + shell tests |
| `jacobdeichert/mask` | 1616 | silent | Markdown-defined CLI task runner; path/command parse | markdown task/path edge + Rust tests |
| `jethrokuan/z` | 1532 | silent | Pure-fish z directory jumping; path/ frecency | fish z path edge + shell tests |
| `isacikgoz/tldr` | 1429 | silent | Fast interactive tldr client; path/page cache | tldr page/path edge + Go tests |
| `philj56/tofi` | 1398 | silent | Tiny dynamic menu for Wayland; config/path | menu config/path edge + C tests |
| `astrand/xclip` | 1323 | silent | X11 clipboard CLI; selection/path | clipboard selection/path edge + C tests |
| `sharkdp/binocle` | 1321 | silent | Graphical binary data visualizer; path/format | binary path/view edge + Rust tests |
| `emersion/slurp` | 1282 | silent | Wayland region selector CLI; output/geometry | region/output edge + C tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `233boy/sing-box` | 4617 | silent | VPN/proxy one-click installer (circumvention adjacency) — leave; not playbook hunk class |
| `monitoror/monitoror` | 4389 | silent | Monitoring wallboard/dashboard product — weak CLI path/quoting hunk class |
| `tmux-plugins/tmux-continuum` | 4067 | silent | tmux plugin not standalone famous CLI product home — leave |
| `01mf02/jaq` | 3744 | hard_ban | CONTRIBUTING forbids machine-generated content (must be human-written) — hard leave |
| `contour-terminal/contour` | 3019 | silent | Full terminal emulator surface — heavy GUI/process; prefer CLI utilities over emulator homes |
| `chjj/compton` | 2263 | silent | Legacy X11 compositor superseded by yshui/picom (already scored) — leave stale fork |

Notes: Prefer product CLI/TUI homes with path/quoting/parser tests (ugrep/xan/ouch/s5cmd/finch/topgrade class). Leave VPN installers, stale compositor forks, wallboards, tmux plugins-only, and full terminal-emulator surfaces. `01mf02/jaq` forbids machine-generated content (hard leave). `neomutt/neomutt` requires AI disclosure.

