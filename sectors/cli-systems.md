# Sector survey: cli-systems

Account: `vulragrag-star` · refreshed `2026-09-08T17:38:01Z` · TS/JS/Zig DevEx slice · No fork/PR/comment.

Playbook lens: parser/path/formatter/LSP/bundler tooling with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 136 | No hard ban in common paths |
| disclosure | 21 | AI disclosure language |
| hard_ban | 4 | Hard AI ban |
| hostility_risk | 1 | Hostility-adjacent |

Proceed: **132** · Leave: **30**.

## PROCEED candidates (contrib fit)

| Repo | Stars | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `ohmyzsh/ohmyzsh` | 189625 | disclosure | disclosure required; zsh framework; plugin/path/quoting | plugin path / quoting edge + shell tests |
| `Genymobile/scrcpy` | 149109 | silent | Android mirror CLI; argv/path/adb | adb path / argv edge + C tests |
| `microsoft/PowerToys` | 138490 | silent | Windows utilities; path/config modules | module path/config edge + C#/C++ tests |
| `fatedier/frp` | 109273 | silent | reverse proxy CLI; config/path | proxy config/path edge + Go tests |
| `microsoft/terminal` | 104843 | silent | Windows Terminal; settings/path/escape | settings JSON path / escape edge + C++ tests |
| `nvbn/thefuck` | 97772 | silent | shell corrector; argv/rule parse | command rule / argv edge + Python tests |
| `nvm-sh/nvm` | 95020 | silent | node version manager; path/shell quoting | NODE_VERSION path / shell quoting + shell tests |
| `junegunn/fzf` | 82865 | silent | fuzzy finder CLI; argv/path/shell integration | shell/argv/path + Go tests |
| `jesseduffield/lazygit` | 82122 | disclosure | disclosure required; git TUI; path/argv/config | git path/config edge + Go tests |
| `Eugeny/tabby` | 74387 | disclosure | PR template AI-usage checklist (not a ban); terminal config/SSH path edges | SSH config / profile path edge + TS tests — check AI level box |
| `BurntSushi/ripgrep` | 68078 | disclosure | disclosure required; search CLI; path/glob/ignore edges with strong Rust tests | path/glob/ignore edge + Rust tests |
| `tw93/Mole` | 66556 | silent | Mac cleanup CLI; path/quoting | path / shell quoting edge + shell tests |
| `pi-hole/pi-hole` | 60796 | silent | DNS sinkhole CLI/scripts; path/quoting | script path / gravity list edge + shell tests |
| `sharkdp/bat` | 60389 | silent | cat clone; path/syntax/theme config | path/theme config edge + Rust tests |
| `starship/starship` | 59811 | disclosure | disclosure required; shell prompt; config/path/module parse | config.toml path/module edge + Rust tests |
| `rclone/rclone` | 59639 | disclosure | disclosure required; cloud sync CLI; path/quoting/remote | remote path/quoting edge + Go tests |
| `FiloSottile/mkcert` | 59563 | silent | local TLS cert CLI; path/CAROOT | CAROOT path / hostname edge + Go tests |
| `PowerShell/PowerShell` | 55292 | silent | shell; path/quoting/parser | path/quoting / parser edge + C# tests |
| `wagoodman/dive` | 54538 | silent | docker image layer explorer; path/argv | image ref / layer path edge + Go tests |
| `Homebrew/brew` | 49467 | disclosure | disclosure required; package manager CLI; formula/path/quoting | formula path / bottle quoting + Ruby tests |
| `Orange-OpenSource/hurl` | 19190 | disclosure | AI Tool Use Policy: tools OK for code; PR/issue/review text must be human-written | Hurlfile parse / path edge + Rust tests — human-written PR text |
| `ginuerzh/gost` | 18214 | silent | tunnel CLI; URL/path/argv | proxy URL / path edge + Go tests |
| `upx/upx` | 17857 | silent | executable packer CLI; path/format | path / format edge + C++ tests |
| `asciinema/asciinema` | 17780 | disclosure | disclosure required; terminal recorder CLI; path/cast | cast path / timing edge + Rust tests |
| `NixOS/nix` | 17655 | disclosure | disclosure required; package manager; path/store/flake | store path / flake ref edge + C++ tests |
| `ImageMagick/ImageMagick` | 17367 | silent | image CLI; argv/path/format | argv / format path edge + C tests |
| `swaywm/sway` | 17312 | silent | Wayland compositor; config/path | config path / command edge + C tests |
| `wtfutil/wtf` | 17077 | silent | terminal dashboard; config/path | config YAML path edge + Go tests |
| `rui314/mold` | 16954 | silent | linker; path/arg/response-file | response-file / path edge + C++ tests |
| `systemd/systemd` | 16666 | disclosure | disclosure required; init/service manager; unit path/parser | unit file path / parser edge + C tests |
| `ffuf/ffuf` | 16652 | silent | web fuzzer CLI; wordlist/path | wordlist path / filter edge + Go tests |
| `davatorium/rofi` | 16375 | silent | launcher/dmenu; path/modi config | modi path / config edge + C tests |
| `lsd-rs/lsd` | 16214 | silent | ls clone; path/color/config | path / config edge + Rust tests |
| `go-task/task` | 16110 | disclosure | AI Usage Policy: disclose AI, human PR text, review/test before submit; Taskfile path/vars | Taskfile path / var quoting edge + Go tests — disclose AI |
| `mikefarah/yq` | 15934 | disclosure | AGENTS.md mandates agent disclosure on GitHub actions; human bugfix PRs with tests welcome | expression / path edge + Go tests — disclose if agent-assisted |
| `winsiderss/systeminformer` | 15898 | silent | Windows sys monitor; path/config | path / config edge + C tests |
| `ast-grep/ast-grep` | 15797 | silent | structural search CLI; rule/path | rule YAML / path edge + Rust tests |
| `cloudflare/cloudflared` | 15543 | silent | tunnel CLI; config/path/argv | tunnel config / ingress path edge + Go tests |
| `benfred/py-spy` | 15481 | silent | Python profiler CLI; path/pid | pid / native path edge + Rust tests |
| `Y2Z/monolith` | 15466 | silent | webpage save CLI; URL/path | URL / asset path edge + Rust tests |
| `direnv/direnv` | 15428 | silent | env dir loader; path/.envrc | .envrc path / stdlib edge + Go tests |
| `volta-cli/volta` | 13054 | silent | JS toolchain manager; path/shim/install edges | toolchain path/shim edge + tests |
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

## LEAVE list

| Repo | Stars | Policy | Reason |
|---|---:|---|---|
| `yt-dlp/yt-dlp` | 189743 | hard_ban | CONTRIBUTING NO AI/NO LLM for issues/PRs/comments |
| `ollama/ollama` | 180445 | silent | LLM runner product — model/docs farm risk; not path/quoting CLI core |
| `anthropics/claude-code` | 144407 | silent | AI coding agent product — agent-farm risk |
| `ytdl-org/youtube-dl` | 141159 | silent | legacy; prefer yt-dlp but yt-dlp is hard_ban — leave both |
| `ggml-org/llama.cpp` | 127449 | disclosure | AI Usage Policy disclosure + no AI for tracker posts; LLM inference — wrong primary hunk class this pass |
| `openai/codex` | 122362 | silent | AI coding agent product — agent-farm / wrong class for systems CLI hunk |
| `google-gemini/gemini-cli` | 106861 | silent | AI coding agent CLI — agent-farm risk |
| `sherlock-project/sherlock` | 91080 | silent | OSINT username hunter — security/OSINT class, not systems path/quoting home |
| `syncthing/syncthing` | 88379 | hostility_risk | CONTRIBUTING rejects wholly/mostly AI-generated contributions; AI issues/comments banned |
| `alacritty/alacritty` | 65657 | hard_ban | CONTRIBUTING: contributions must not include LLM/probabilistic-tool content (code/docs/PRs/issues/comments) |
| `FFmpeg/FFmpeg` | 64031 | silent | famous systems; mailing-list/heavy process — park for new-account first home |
| `ghostty-org/ghostty` | 60832 | hard_ban | Ghostty AI_POLICY vouch system — hard leave |
| `termux/termux-app` | 60491 | silent | Android terminal app platform — heavy mobile process, not desktop CLI hunk home |
| `Textualize/rich` | 57343 | disclosure | AI_POLICY: AI PRs only after maintainer-approved issue; library not end-user CLI product home |
| `romkatv/powerlevel10k` | 55054 | silent | zsh theme — config cosmetics, weak regression-test product surface |
| `hashicorp/terraform` | 49634 | silent | IaC product better fits devops-build; heavy HashiCorp process |
| `google/zx` | 45733 | silent | Scripting utility - prefer package/toolchain CLIs |
| `denisidoro/navi` | 17526 | silent | interactive cheatsheet CLI — docs/cheat farm risk, weak systems hunk class |
| `clap-rs/clap` | 16691 | silent | argument-parser library not end-user CLI product home |
| `libsdl-org/SDL` | 16526 | hard_ban | SDL: AI must not generate contribution code |
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

## Sector synthesis

- Refreshed after TS/JS/Zig DevEx product slice.
- No tracker comments/forks/third-party PRs.
- scored_at: `2026-09-08T17:38:01Z`
