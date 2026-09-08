# Sector survey: cli-systems

Account: `vulragrag-star` · Input: `survey/raw/cli-systems.jsonl` (350 repos; heavy awesome/AI-agent/tutorial noise) · Deep-sampled **60** CLI/systems products via `gh api` contents (CONTRIBUTING/AI_POLICY/AGENTS/PR templates) · Hard leaves + predecessor closed/open queues respected · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **CLI argv / path / quoting / config-parser / shell-integration bugs with regression tests** (fzf/ripgrep/rclone/task/yq/direnv class — not AI coding agents, not awesome-lists, not LLM runners, not library-only clap/rich).

## Policy histogram (deep sample of 60)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 40 | Most classic CLIs still have no hard AI ban page |
| disclosure | 15 | ripgrep, starship, lazygit, rclone, ohmyzsh, brew, nix, systemd, asciinema, yq, go-task, tabby, hurl, … |
| hostility_risk | 1 | syncthing rejects wholly/mostly AI-generated patches |
| hard_ban | 4 | alacritty, yt-dlp, ghostty (vouch), SDL |
| agentscan | 0 | None in this 60-repo sample |

Proceed: **41** · Leave: **19** · Scored lines appended to `survey/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class (CLI path/quoting/parser + tests). Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork. **Do not steal** predecessor open queues (`denoland/deno`, `go-gitea/gitea`, `apache/nuttx`, `tianocore/edk2`, `mesonbuild/meson`, `pypa/hatch`).

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `junegunn/fzf` | 82865 | silent | fuzzy finder CLI; argv/path/shell integration | shell/argv/path + Go tests |
| `BurntSushi/ripgrep` | 68078 | disclosure | search CLI; path/glob/ignore edges with strong Rust tests — disclose AI | path/glob/ignore edge + Rust tests |
| `jesseduffield/lazygit` | 82122 | disclosure | git TUI; path/argv/config — disclose AI | git path/config edge + Go tests |
| `sharkdp/bat` | 60389 | silent | cat clone; path/syntax/theme config | path/theme config edge + Rust tests |
| `starship/starship` | 59811 | disclosure | shell prompt; config/path/module parse — disclose AI | config.toml path/module edge + Rust tests |
| `rclone/rclone` | 59639 | disclosure | cloud sync CLI; path/quoting/remote — disclose AI | remote path/quoting edge + Go tests |
| `direnv/direnv` | 15428 | silent | env dir loader; path/.envrc | .envrc path / stdlib edge + Go tests |
| `go-task/task` | 16110 | disclosure | AI Usage Policy: disclose AI, human PR text, review/test before submit; Taskfile path/vars | Taskfile path / var quoting edge + Go tests — disclose AI |
| `mikefarah/yq` | 15934 | disclosure | AGENTS.md mandates agent disclosure on GitHub actions; human bugfix PRs with tests welcome | expression / path edge + Go tests — disclose if agent-assisted |
| `lsd-rs/lsd` | 16214 | silent | ls clone; path/color/config | path / config edge + Rust tests |
| `FiloSottile/mkcert` | 59563 | silent | local TLS cert CLI; path/CAROOT | CAROOT path / hostname edge + Go tests |
| `wagoodman/dive` | 54538 | silent | docker image layer explorer; path/argv | image ref / layer path edge + Go tests |
| `Y2Z/monolith` | 15466 | silent | webpage save CLI; URL/path | URL / asset path edge + Rust tests |
| `ast-grep/ast-grep` | 15797 | silent | structural search CLI; rule/path | rule YAML / path edge + Rust tests |
| `Orange-OpenSource/hurl` | 19190 | disclosure | AI Tool Use Policy: tools OK for code; PR/issue/review text must be human-written | Hurlfile parse / path edge + Rust tests — human-written PR text |
| `asciinema/asciinema` | 17780 | disclosure | terminal recorder CLI; path/cast — disclose AI | cast path / timing edge + Rust tests |
| `ffuf/ffuf` | 16652 | silent | web fuzzer CLI; wordlist/path | wordlist path / filter edge + Go tests |
| `benfred/py-spy` | 15481 | silent | Python profiler CLI; path/pid | pid / native path edge + Rust tests |
| `rui314/mold` | 16954 | silent | linker; path/arg/response-file | response-file / path edge + C++ tests |
| `upx/upx` | 17857 | silent | executable packer CLI; path/format | path / format edge + C++ tests |
| `fatedier/frp` | 109273 | silent | reverse proxy CLI; config/path | proxy config/path edge + Go tests |
| `cloudflare/cloudflared` | 15543 | silent | tunnel CLI; config/path/argv | tunnel config / ingress path edge + Go tests |
| `ginuerzh/gost` | 18214 | silent | tunnel CLI; URL/path/argv | proxy URL / path edge + Go tests |
| `Genymobile/scrcpy` | 149109 | silent | Android mirror CLI; argv/path/adb | adb path / argv edge + C tests |
| `nvm-sh/nvm` | 95020 | silent | node version manager; path/shell quoting | NODE_VERSION path / shell quoting + shell tests |
| `nvbn/thefuck` | 97772 | silent | shell corrector; argv/rule parse | command rule / argv edge + Python tests |
| `ohmyzsh/ohmyzsh` | 189625 | disclosure | zsh framework; plugin/path/quoting — disclose AI | plugin path / quoting edge + shell tests |
| `Homebrew/brew` | 49467 | disclosure | package manager CLI; formula/path/quoting — disclose AI | formula path / bottle quoting + Ruby tests |
| `davatorium/rofi` | 16375 | silent | launcher/dmenu; path/modi config | modi path / config edge + C tests |
| `swaywm/sway` | 17312 | silent | Wayland compositor; config/path | config path / command edge + C tests |
| `wtfutil/wtf` | 17077 | silent | terminal dashboard; config/path | config YAML path edge + Go tests |
| `tw93/Mole` | 66556 | silent | Mac cleanup CLI; path/quoting | path / shell quoting edge + shell tests |
| `Eugeny/tabby` | 74387 | disclosure | PR template AI-usage checklist (not a ban); terminal config/SSH path edges | SSH config / profile path edge + TS tests — check AI level box |
| `pi-hole/pi-hole` | 60796 | silent | DNS sinkhole CLI/scripts; path/quoting | script path / gravity list edge + shell tests |
| `microsoft/terminal` | 104843 | silent | Windows Terminal; settings/path/escape | settings JSON path / escape edge + C++ tests |
| `microsoft/PowerToys` | 138490 | silent | Windows utilities; path/config modules | module path/config edge + C#/C++ tests |
| `PowerShell/PowerShell` | 55292 | silent | shell; path/quoting/parser | path/quoting / parser edge + C# tests |
| `NixOS/nix` | 17655 | disclosure | package manager; path/store/flake — disclose AI | store path / flake ref edge + C++ tests |
| `systemd/systemd` | 16666 | disclosure | init/service manager; unit path/parser — disclose AI | unit file path / parser edge + C tests |
| `ImageMagick/ImageMagick` | 17367 | silent | image CLI; argv/path/format | argv / format path edge + C tests |
| `winsiderss/systeminformer` | 15898 | silent | Windows sys monitor; path/config | path / config edge + C tests |

### Tier notes

**Best first homes (small testable CLI path/quoting/parser hunks):**

1. `junegunn/fzf` — silent; shell integration / argv / path edges.
2. `BurntSushi/ripgrep` — **AI_POLICY**: AI for code OK; no AI for tracker comments; no autonomous agents; disclose.
3. `direnv/direnv` / `go-task/task` / `mikefarah/yq` — env/task/YAML CLIs; task+yq need disclosure / human PR text.
4. `sharkdp/bat` / `lsd-rs/lsd` / `Y2Z/monolith` — small Rust CLIs; path/config edges.
5. `jesseduffield/lazygit` — disclosure culture; git TUI path/config; high AI-PR fatigue — keep tiny + tested.
6. `FiloSottile/mkcert` / `wagoodman/dive` / `benfred/py-spy` / `ffuf/ffuf` — focused Go/Rust CLIs.
7. `rclone/rclone` — **disclose AI**; human owns every line; cloud path/quoting.
8. `starship/starship` — **AI_POLICY** (Ghostty/LLVM-inspired): disclose in PR template; no AI for GFI; no raw LLM replies.
9. `Orange-OpenSource/hurl` — tools OK; **human-written** issues/PR/review text.
10. `ast-grep/ast-grep` / `rui314/mold` / `upx/upx` — structural search / linker / packer path edges.

**Careful / later (disclosure or process friction):**

- `ohmyzsh/ohmyzsh` — disclose meaningful AI; quality bar; decline unreviewed AI.
- `Homebrew/brew` — Responsible AI Usage: disclose model; no AI trailers; non-maintainers **one AI PR at a time**; answer reviews yourself without AI.
- `NixOS/nix` — Automation/AI policy: responsible human + `Assisted-by:` trailer with tool/model/version.
- `systemd/systemd` — LLM policy in docs; human ownership; no AI-as-author trailers.
- `asciinema/asciinema` — note AI tool in PR description.
- `Eugeny/tabby` — check AI-involvement level in PR template.
- `microsoft/terminal`, `microsoft/PowerToys`, `PowerShell/PowerShell` — large Microsoft surfaces / CLA; not first-home.
- `ImageMagick/ImageMagick`, `winsiderss/systeminformer`, `pi-hole/pi-hole` — large or script-heavy; verify activity + outsider PR voice first.
- `fatedier/frp` / `cloudflare/cloudflared` / `ginuerzh/gost` — tunnel CLIs (also networking-adjacent).
- `Genymobile/scrcpy` — C/adb; strong product but mobile-host coupling.
- `nvm-sh/nvm` / `nvbn/thefuck` / `tw93/Mole` — shell path/quoting; check maintenance cadence.
- `davatorium/rofi` / `swaywm/sway` — Wayland/X11 launcher/compositor config edges.

**Clusters to farm leftovers (one home at a time):**

| Cluster | Repos | Hunk shape |
|---|---|---|
| Search / filter CLIs | fzf, ripgrep, ast-grep, bat, lsd, yq | path/glob/ignore / expression |
| Shell / env | direnv, ohmyzsh, nvm, thefuck, starship | .envrc / plugin path / quoting |
| Task / HTTP / sync | go-task, hurl, rclone, asciinema, monolith | Taskfile / Hurlfile / remote path |
| Containers / certs / fuzz | dive, mkcert, ffuf, py-spy | image ref / CAROOT / wordlist path |
| Systems binaries | mold, upx, scrcpy, ImageMagick | response-file / format / adb argv |
| Tunnels | frp, cloudflared, gost | config/URL/path |
| Terminals / WM | tabby, rofi, sway, Windows Terminal | config/SSH/modi path |

## LEAVE list

| Repo | ★ | Policy | Reason |
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
| `denisidoro/navi` | 17526 | silent | interactive cheatsheet CLI — docs/cheat farm risk, weak systems hunk class |
| `clap-rs/clap` | 16691 | silent | argument-parser library not end-user CLI product home |
| `libsdl-org/SDL` | 16526 | hard_ban | SDL: AI must not generate contribution code |

## Shard noise (not deep-sampled)

Raw `cli-systems.jsonl` also contains high-★ awesome/curriculum dumps (`awesome-selfhosted`, `the-book-of-secret-knowledge`, `TheAlgorithms/*`, beginner courses), AI agent/skills farms (`openclaw`, `obra/superpowers`, `mattpocock/skills`, `anthropics/*`, `cline`, `warp`, `paperclipai`), and apps only loosely CLI-adjacent (Flutter, VS Code, ComfyUI, Immich, etc.). Those were skipped for deep policy work — not systems CLI product homes.

## Hard excludes honored

- **Hard leave patterns:** Cython, OpenJDK, Zig LLM ban, SQLite agentic, Godot, Gentoo, QEMU AI decline, Ghostty vouch, AgentScan adopters — none of Cython/OpenJDK/Zig/SQLite/Godot/Gentoo/QEMU/AgentScan products appeared as proceed in this sample; **Ghostty** and **SDL** scored leave; **yt-dlp** / **alacritty** hard_ban.
- **Predecessor closed queues:** vitest / mise / pypa / cibuildwheel / awesome-copilot / fauxnix — not targeted.
- **Do not steal open queues:** deno / gitea / nuttx / edk2 / meson / hatch — not in this sector proceed list (deno lives under compilers-runtimes leave).

## Method notes

- Policy files fetched with `gh api repos/.../contents/... -H Accept: application/vnd.github.raw` (60-repo deep sample).
- False-positive fix: `go-task/task` initially matched `hard_ban` on PR-template “(No AI)” phrase; live [AI Usage Policy](https://taskfile.dev/docs/contributing#ai-usage-policy) is **disclosure**, not ban.
- `mikefarah/yq` disclosure signal is primarily `AGENTS.md` (mandatory agent disclosure); human CONTRIBUTING still welcomes bugfix PRs with tests.
- AgentScan: local adopters/blacklist — **0 hits** in this 60-repo sample.
- No tracker comments, forks, or third-party PRs from this survey pass.
- scored_at: `2026-09-08T08:18:20Z`
