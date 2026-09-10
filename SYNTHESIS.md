# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **1501**
- Proceed: **1026**
- Mid-band (1k–5k★) scored: **949** (proceed 712)
- By sector: {'python-tooling': 151, 'security-crypto': 166, 'cli-systems': 290, 'editors-devex': 175, 'compilers-runtimes': 184, 'databases-storage': 147, 'networking-distributed': 236, 'devops-build': 152}
- Policy mix: {'silent': 1345, 'hard_ban': 18, 'disclosure': 107, 'hostility_risk': 26, 'agentscan': 5}
- Language mix (universe top): {'Go': 2520, 'C++': 2413, 'Python': 2287, 'TypeScript': 2252, 'Rust': 2133, 'C': 2093, 'JavaScript': 2009, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **famous editors/shells score** (+52 scored, 33 proceed) — tmux, helix, bubbletea, lapce, k9s, micro, coc.nvim, gum, superfile, ratatui, nnn, telescope.nvim, tpm, tview, tmux-resu…
- Mid-band language fill: TypeScript **2252**, JavaScript **2009**, Zig **51**, Rust **2133**, Go **2520** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Famous shells/editors gap fill (tmux/helix/lapce/micro + bubbletea/ratatui/tview + nnn/lf/superfile/gum/k9s) is now scored; full terminal emulators (kitty/wezterm/rio/warp/hyper/waveterm) left as emulator surfaces. Disclosure homes (ratatui, visidata, waveterm leave) need human-owned PR bodies where proceeding.
TS/JS/Zig product homes (eslint/stylelint/bundlers/ts-node/tsx/tsup/husky/commitlint/zls) remain on the shortlist. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits, rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, mrcjkb/rustaceanvim no-LLM, jfecher/ante NO-AI, boxlite-ai/boxlite NO-AI, 01mf02/jaq machine-generated ban. Zig-lang itself remains a hard leave (no-LLM CONTRIBUTING); zigtools/zls is separately proceed. Famous CLI pass left cheat.sh / oh-my-posh / oils. This editors-shells pass left kitty/wezterm/rio/warp/hyper/waveterm (emulator), vscode/VSCodium/neovide (IDE/GUI), crush/aider (agent products), textual (maintainer-approved AI issue gate), zsh (full shell), spaceship/oh-my-tmux (theme/config).

## Next
Rebuild SHORTLIST after this famous editors/shells score (done in same commit). Next atlas slice: deepen **networking-distributed midband leftovers**, or other unfinished midband pockets. Contribution cadence remains separate from atlas literature work.
