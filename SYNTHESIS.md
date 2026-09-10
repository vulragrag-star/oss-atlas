# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **1449**
- Proceed: **993**
- Mid-band (1k–5k★) scored: **941** (proceed 707)
- By sector: {'python-tooling': 151, 'security-crypto': 166, 'cli-systems': 261, 'editors-devex': 152, 'compilers-runtimes': 184, 'databases-storage': 147, 'networking-distributed': 236, 'devops-build': 152}
- Policy mix: {'silent': 1297, 'hard_ban': 18, 'disclosure': 103, 'hostility_risk': 26, 'agentscan': 5}
- Language mix (universe top): {'Go': 2520, 'C++': 2413, 'Python': 2287, 'TypeScript': 2252, 'Rust': 2133, 'C': 2093, 'JavaScript': 2009, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **famous CLI score** (+50 scored, 47 proceed) — cli, fd, yazi, nushell, wrk, croc, shellcheck, zoxide, cli, just, jq…
- Mid-band language fill: TypeScript **2252**, JavaScript **2009**, Zig **51**, Rust **2133**, Go **2520** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter homes.
The famous product CLI gap fill (fd/eza/delta/zoxide/yazi/mise/btop/zellij/just/jq/gh, shell history, du/ps/bench, version managers) is now scored into `scored.jsonl` with cli-systems digests refreshed. Several homes require disclosure / human-owned PR bodies (yazi, btop, bottom, difftastic, fd, mise, uutils, miller).
TS/JS/Zig product homes (eslint/stylelint/bundlers/ts-node/tsx/tsup/husky/commitlint/zls) remain on the shortlist. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits, rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, mrcjkb/rustaceanvim no-LLM, jfecher/ante NO-AI, boxlite-ai/boxlite NO-AI, 01mf02/jaq machine-generated ban. Zig-lang itself remains a hard leave (no-LLM CONTRIBUTING); zigtools/zls is separately proceed. This pass also left cheat.sh (content service), oh-my-posh (prompt themes), and oils (full language megaproject).

## Next
Rebuild SHORTLIST after this famous-CLI score (done in same commit). Next atlas slice: deepen networking-distributed midband leftovers, or score adjacent famous shells/editors still unscored (tmux/helix/lapce/kitty) into the right sectors. Contribution cadence remains separate from atlas literature work.
