# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **1399**
- Proceed: **946**
- Mid-band (1k–5k★) scored: **937** (proceed 704)
- By sector: {'python-tooling': 151, 'security-crypto': 166, 'cli-systems': 211, 'editors-devex': 152, 'compilers-runtimes': 184, 'databases-storage': 147, 'networking-distributed': 236, 'devops-build': 152}
- Policy mix: {'silent': 1256, 'hard_ban': 18, 'disclosure': 94, 'hostility_risk': 26, 'agentscan': 5}
- Language mix (universe top): {'Go': 2520, 'C++': 2413, 'Python': 2287, 'TypeScript': 2252, 'Rust': 2133, 'C': 2093, 'JavaScript': 2009, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **universe expand** (+810 repos) — filled under-paged ≥20k Rust/Go/C/C++/Python/Shell harvest + famous CLI product gaps (fd/eza/delta/zoxide/yazi/mise/btop/zellij/just/jq/gh/glow/vhs/bubbletea/atuin/tmux/helix/wezterm/nushell/difftastic/…) and topic:cli/tui midband Go/Rust leftovers
- Mid-band language fill: TypeScript **2252**, JavaScript **2009**, Zig **51**, Rust **2133**, Go **2520** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter homes.
Mid-band (1k–5k★) expands the map beyond megastar repos — same gates, smaller surfaces. All eight sectors have midband digests. Famous product CLIs that the first harvest under-paged (fd/eza/delta/zoxide/yazi/mise/btop/zellij class) are now in `data/universe.jsonl` and ready for a scoring pass — they were not yet batch-scored in this slice.
TS/JS/Zig product homes (eslint/stylelint/bundlers/ts-node/tsx/tsup/husky/commitlint/zls) remain on the shortlist. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits, rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, mrcjkb/rustaceanvim no-LLM, jfecher/ante NO-AI, boxlite-ai/boxlite NO-AI, 01mf02/jaq machine-generated ban. Zig-lang itself remains a hard leave (no-LLM CONTRIBUTING); zigtools/zls is separately proceed.

## Next
Score the newly added famous CLI / systems product slice into `scored.jsonl` + refresh cli-systems (and adjacent) digests. Networking midband leftovers are nearly exhausted (2 raw unscored). Contribution cadence remains separate from atlas literature work.
