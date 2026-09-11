# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2017**
- Proceed: **1386**
- Mid-band (1k–5k★) scored: **1114** (proceed 827)
- By sector: {'python-tooling': 216, 'security-crypto': 270, 'cli-systems': 290, 'editors-devex': 283, 'compilers-runtimes': 287, 'databases-storage': 217, 'networking-distributed': 236, 'devops-build': 218}
- Policy mix: {'silent': 1780, 'hard_ban': 24, 'disclosure': 169, 'hostility_risk': 30, 'agentscan': 14}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **compilers-runtimes product deepen** (+103 scored, 64 proceed) — julia, v, emscripten, elixir, RustPython, micropython, gleam, wasmer, crystal, wenyan, Nim, assemblyscript, otp, Odin, hermes, sdk, quickjs,…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Compilers-runtimes product deepen scored Wasm toolchains/runtimes (wasmer/WasmEdge/wasm3/binaryen/wabt/wasm-tools/wasm-pack/AssemblyScript/spin), embeddable engines (quickjs/hermes/LuaJIT/luau/wren), and mid-size languages (gleam/crystal/nim/elixir/julia/odin/v/grain/rescript/purescript/elm/cython/micropython/RustPython). Leave AgentScan nodejs, hard bans (zig/godot/OpenJDK/solidity), mentor-gated perl5, language megas (go/swift/llvm/gcc/php/ruby/v8/roslyn), proof assistants, agent langs (baml), and browser emulators. Disclosure/careful: Julia/elixir/RustPython/micropython/dart/WasmEdge/ocaml.
Editors-devex + security-crypto product deepens remain scored; full terminal emulators stay leave. Continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Note: certbot/authentik scanner NO-AI hits were false positives (AI allowed with disclosure/HITL); Zettlr CoC-only AI mention overridden to silent.

## Next
Next thin tail: networking-distributed product deepen; rebuild SHORTLIST/SYNTHESIS already refreshed this pass. Contribution cadence remains separate from atlas literature work.
