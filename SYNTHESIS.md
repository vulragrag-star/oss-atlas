# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **16334** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **1113**
- Proceed: **724**
- Mid-band (1k–5k★) scored: **651** (proceed 482)
- By sector: {'python-tooling': 116, 'security-crypto': 126, 'cli-systems': 162, 'editors-devex': 108, 'compilers-runtimes': 140, 'databases-storage': 107, 'networking-distributed': 236, 'devops-build': 118}
- Policy mix: {'silent': 986, 'hard_ban': 14, 'disclosure': 82, 'hostility_risk': 26, 'agentscan': 5}
- Language mix (universe top): {'C++': 2340, 'Go': 2298, 'TypeScript': 2252, 'C': 2039, 'Rust': 2023, 'JavaScript': 2009, 'Python': 1982, 'Shell': 1208, 'Zig': 51, '?': 46}
- Latest slice: TS/JS/Zig DevEx product scoring (+37 scores; proceed 24 / leave 13); editors-devex now **108**
- Mid-band language fill: TypeScript **939**, JavaScript **864**, Zig **42** (plus prior Rust/Go/C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING.
Mid-band (1k–5k★) expands the map beyond megastar repos — same gates, smaller surfaces. All eight sectors now have midband digests.
TS/JS/Zig universe fill is now being scored into product homes: editors-devex deepened with eslint/stylelint/bundlers/ts-node/tsx/tsup/zls/husky/commitlint; minority spill into cli-systems / devops-build / compilers-runtimes. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits, rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban. Zig-lang itself remains a hard leave (no-LLM CONTRIBUTING); zigtools/zls is separately proceed.

## Next
Refresh SHORTLIST.md toward ~100 from new proceed density (especially editors-devex + devops-build package/toolchain homes). Optionally add missing high-signal tools still absent from universe, then score. Contribution cadence remains separate from atlas literature work.
