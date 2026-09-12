# Synthesis

Living directional read of the atlas (auto-refreshed).

## Coverage now
- Universe: **17144** repos (≥1k★ systems-leaning; includes 1k–5k mid-band)
- Scored repos (unique): **2833**
- Proceed: **1944**
- Mid-band (1k–5k★) scored: **1525** (proceed 1111)
- By sector: {'python-tooling': 353, 'security-crypto': 363, 'cli-systems': 378, 'editors-devex': 353, 'compilers-runtimes': 376, 'databases-storage': 335, 'networking-distributed': 356, 'devops-build': 319}
- Policy mix: {'silent': 2501, 'hard_ban': 35, 'disclosure': 245, 'hostility_risk': 33, 'agentscan': 19}
- Language mix (universe top): {'Go': 2519, 'C++': 2413, 'Python': 2288, 'TypeScript': 2253, 'Rust': 2129, 'C': 2092, 'JavaScript': 2010, 'Shell': 1243, 'Zig': 51, '?': 46}
- Latest slice: **compilers-runtimes midband product deepen** (+89 scored, 69 proceed) — cosmopolitan, antlr4, pyodide, mono, unicorn, blink, ChezScheme, cxx, wazero, slang, box64, mruby, ohm, pest, rust-bindgen, wuffs, c2rust, 86Box, chisel, yosys,…
- Mid-band language fill: TypeScript **2253**, JavaScript **2010**, Zig **51**, Rust **2129**, Go **2519** (plus C/C++/Python/Shell)

## Working thesis
Primary farm: **systems CLI + build/packaging adjacency** (path/quoting/parser bugs with tests).
Secondary: SQL/query/storage CLIs, selective WASM/runtimes/small languages, networking protocol/CLI tools, careful security tooling with clear CONTRIBUTING, and DevEx LSP/formatter/editor homes.
Compilers-runtimes midband product deepen scored language/Wasm/JIT/interpreter/assembler/userspace-emulator/shader/HDL/bindgen homes (cosmopolitan/antlr/pyodide/mono/unicorn/blink/ChezScheme/cxx/wazero/slang/box64/mruby/pest/bindgen/wuffs/c2rust/86Box/chisel/yosys/scala-js/nasm/Spike/openj9/DynamoRIO/ghdl/teal/chevrotain/graaljs/SPIRV/veryl). Leave capstone/FEX hard bans, brython/skulpt toys, scriptc/mint novelty, Triton/miasm RE spills, CompCert academic, tinyexpr/elk. Disclosure: cosmopolitan, slang, box64, 86Box, chisel, glslang, openj9, dynamorio, veryl.
Prior cli-systems/editors/devops/python/DB/networking/security midband product deepens remain scored; continue avoiding web-app noise and AgentScan circles.

## Hard leaves seen in survey
sqlite (agentic ban), typst, kanidm, openbao, fish-shell, qemu/gimp, alacritty/yt-dlp/ghostty/SDL, PowerDNS/ipxe AI bans, AgentScan hits (incl. nodejs/vite/storybook/babel/biome/mocha/vitest/changesets/svelte/sqlfluff/unplugin/gritql), rustc/miri mentor-gated LLM lanes, nasa/spacewasm AI-in-src ban, cloud-hypervisor mentor-gated LLM, anomalyco/opencode NO-AI, argotorg/solidity NO-AI, OpenJDK GB interim ban, Godot agent ban. Zig-lang itself remains a hard leave (no-LLM); zigtools/zls is separately proceed. Networking deepen: grpc NO-AI, rabbitmq NO-AI, kube-router NO-AI, AgentScan undici. DB deepen-3 / Python deepen-2 leaves retained. DevOps deepen-2: kueue scanner hard_ban overridden to disclosure (K8s AI policy); s6-overlay disclosure overridden to hard_ban (no LLM contrib). Editors midband deepen: rolldown/tsdown NO-AI, loeffel-io/ls-lint NO-AI. CLI-systems midband product deepen retained. Compilers-runtimes midband product deepen: hard_ban capstone-engine/capstone (forbids AI), FEX-Emu/FEX (NO-AI); capstone-engine/capstone, FEX-Emu/FEX.

## Next
Next: SHORTLIST maintenance / selective universe gap fills / thin midband remainder; contribution cadence remains separate from atlas literature work.
