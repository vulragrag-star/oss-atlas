# Sector survey: compilers-runtimes (mid-band 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/compilers-runtimes-midband.jsonl` · Deep-sampled **79** real product repos (policy via `raw.githubusercontent.com` + workflow names) · Scored **79** lines (**63** proceed / **16** leave) · Band: `1k-5k` · No fork/PR/comment.

Playbook lens: famous main product (1k–5k★), not AgentScan, not hard AI ban, hunk class = **compiler/runtime/parser/path/build bugs with regression tests** (languages, wasm/JIT VMs, OCI runtimes, compiler caches — not ML mega-compilers, not tutorial interpreters, not LLM-demo novelty).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 73 | No hard ban found in common CONTRIBUTING/AI paths |
| disclosure | 3 | Explicit AI-assisted / disclosure language (or org AI policy) |
| hostility_risk | 3 | Hostile or mentor-gated AI posture |

Proceed: **63** · Leave: **16** · Scored lines appended to `survey/scored.jsonl` with `band:"1k-5k"`.

## Hard leaves (playbook — even if outside this band sample)

- `typst/typst` — CONTRIBUTING forbids AI-implemented contributions (higher band; already scored leave)
- `rust-lang/rust` / Miri — forge mentor-gated LLM (`llm-assisted` + pre-arranged mentor); leave for new-account drive-by
- `rust-lang/rustc_codegen_cranelift` / `rustc_codegen_gcc` — same forge LLM posture (in this midband sample → leave)
- Predecessor open queues (e.g. denoland/deno) — do not steal
- AgentScan adopter orgs — leave entire owner tree

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `mozilla/uniffi-rs` | 4942 | silent | Multi-language Rust bindings generator; IDL/path edges | UniFFI IDL/bindings path edge + Rust tests |
| `lunatic-solutions/lunatic` | 4886 | silent | Erlang-inspired Wasm runtime | runtime/process/path edge + Rust tests |
| `ProvableHQ/leo` | 4823 | silent | Leo ZK language compiler; parser/typecheck edges | parser/typecheck edge + Rust tests |
| `aya-rs/aya` | 4797 | silent | Rust eBPF library/runtime (aya) | eBPF program/path edge + Rust tests |
| `PerryTS/perry` | 4775 | silent | Native TS/JS compiler in Rust | parser/emit/path edge + Rust tests |
| `yoav-lavi/melody` | 4744 | silent | Melody→regex compiler language | Melody parse/compile fixture edge + Rust tests |
| `borgo-lang/borgo` | 4636 | silent | Statically typed language compiling to Go | parser/codegen edge + tests |
| `asmjit/asmjit` | 4601 | silent | Low-latency machine-code generation / JIT | assembler API/path edge + C++ tests |
| `marcobambini/gravity` | 4564 | silent | Gravity language + bytecode VM | parser/VM edge + C tests |
| `andreasfertig/cppinsights` | 4522 | silent | C++ Insights compiler-view tool | AST rewrite/path edge + C++ tests |
| `janet-lang/janet` | 4408 | silent | Janet dynamic language + bytecode VM | parser/VM/path edge + C tests |
| `trunk-rs/trunk` | 4389 | silent | Rust Wasm build/bundle/ship CLI | CLI path/asset/config edge + Rust tests |
| `root-project/cling` | 4189 | silent | Cling C++ interpreter (ROOT) | interpreter/path/REPL edge + tests |
| `containers/crun` | 4109 | silent | OCI container runtime (C) | runtime config/path/OCI edge + tests |
| `nestybox/sysbox` | 3855 | silent | Rootless container runtime (runc-class) | runtime config/path edge + tests |
| `d5/tengo` | 3835 | silent | Fast script language for Go | parser/eval edge + Go tests |
| `microsoft/DirectXShaderCompiler` | 3646 | silent | DXC shader compiler (LLVM/Clang-based) | HLSL parse/codegen edge + tests |
| `leafo/moonscript` | 3466 | silent | MoonScript→Lua compiler | parser/compile fixture edge + tests |
| `Shopify/go-lua` | 3454 | silent | Lua VM in Go | VM/API edge + Go tests |
| `gluon-lang/gluon` | 3442 | silent | Embeddable typed language in Rust | parser/typecheck edge + Rust tests |
| `Rust-GPU/rust-gpu` | 3332 | silent | Rust→GPU shader ecosystem | shader codegen/path edge + Rust tests |
| `jank-lang/jank` | 3328 | silent | Native Clojure dialect with C++ interop | parser/interop edge + tests |
| `checkedc/checkedc` | 3259 | silent | Checked C language extension | bounds annotation/parse edge + tests |
| `grame-cncm/faust` | 3147 | silent | Faust DSP language compiler | DSP parse/codegen edge + tests |
| `saghul/txiki.js` | 3142 | silent | Tiny JavaScript runtime | runtime/API/path edge + C tests |
| `ChaiScript/ChaiScript` | 3127 | silent | Embedded C++ scripting language | parser/eval edge + C++ tests |
| `TinyCC/tinycc` | 3030 | silent | Tiny C Compiler | compile/link/path edge + tests |
| `SerenityOS/jakt` | 2987 | silent | Jakt programming language | parser/codegen edge + tests |
| `espruino/Espruino` | 2969 | silent | Espruino JS interpreter for MCUs | parser/API/path edge + C tests |
| `ccache/ccache` | 2953 | silent | Compiler cache — classic path/argv product | cache key/path/argv edge + C++ tests |
| `ispc/ispc` | 2949 | silent | Intel Implicit SPMD Program Compiler | parse/codegen/target edge + tests |
| `wasmerio/wasmer-go` | 2949 | silent | Wasmer Wasm runtime Go bindings/product surface | runtime/API/path edge + Go tests |
| `Rust-GCC/gccrs` | 2940 | silent | GCC frontend for Rust | parse/lowering edge + tests |
| `terralang/terra` | 2907 | silent | Terra low-level lang embedded in Lua | parser/meta edge + tests |
| `erg-lang/erg` | 2859 | silent | Statically typed Python-compatible language | parser/typecheck edge + Rust tests |
| `beefytech/Beef` | 2844 | silent | Beef programming language | parser/codegen edge + tests |
| `IoLanguage/io` | 2791 | silent | Io programming language | parser/VM edge + C tests |
| `container2wasm/container2wasm` | 2782 | silent | Container→Wasm converter | image/path/OCI→wasm edge + Go tests |
| `WAVM/WAVM` | 2777 | silent | WebAssembly Virtual Machine | wasm decode/runtime edge + tests |
| `bytecodealliance/javy` | 2744 | disclosure | JS→Wasm toolchain (BA AI policy: human-in-loop) | JS/wasm toolchain path edge + tests — BA human-in-loop |
| `aardappel/lobster` | 2734 | silent | Lobster programming language | parser/VM edge + tests |
| `wasmi-labs/wasmi` | 2292 | silent | Embeddable Wasm interpreter | wasm decode/host edge + Rust tests |
| `pocketpy/pocketpy` | 2114 | silent | Portable Python interpreter in C | parser/runtime edge + C tests |
| `wa-lang/wa` | 1768 | silent | Wa programming language | parser/codegen edge + Go tests |
| `pikasTech/PikaPython` | 1753 | silent | Ultra-light Python interpreter | parser/runtime edge + C tests |
| `lcompilers/lpython` | 1630 | silent | LPython compiler | parser/ASR/codegen edge + tests |
| `ThakeeNathees/pocketlang` | 1550 | silent | Lightweight embeddable scripting language | parser/VM edge + C tests |
| `VKCOM/kphp` | 1526 | silent | KPHP PHP compiler | PHP parse/codegen edge + tests |
| `bytecodealliance/wit-bindgen` | 1454 | disclosure | WIT bindings generator (BA AI policy) | WIT parse/bindgen path edge + tests — BA human-in-loop |
| `openresty/luajit2` | 1445 | silent | OpenResty LuaJIT 2 branch | JIT/API/path edge + tests |
| `noir-lang/noir` | 1397 | silent | Noir ZK DSL compiler | parser/typecheck edge + Rust tests |
| `hyperledger-solang/solang` | 1382 | silent | Solidity compiler for Solana/Polkadot/Stellar | Solidity parse/codegen edge + Rust tests |
| `tensor-compiler/taco` | 1367 | silent | Tensor Algebra Compiler | tensor expr/parse/codegen edge + tests |
| `Hans-Halverson/brimstone` | 1320 | silent | New JS engine in Rust | parser/VM edge + Rust tests |
| `inko-lang/inko` | 1301 | silent | Concurrent language runtime/compiler | parser/runtime edge + Rust tests |
| `dibyendumajumdar/ravi` | 1254 | silent | Lua dialect with optional typing + JIT/AOT | parser/typing/JIT edge + C tests |
| `morganstanley/hobbes` | 1228 | silent | Language + embedded JIT | parse/JIT edge + tests |
| `vlm/asn1c` | 1175 | silent | ASN.1 compiler | ASN.1 parse/codegen edge + C tests |
| `GaijinEntertainment/daScript` | 1164 | silent | daslang scripting language | parser/VM edge + tests |
| `cloudflare/wirefilter` | 1157 | silent | Wireshark-like filter execution engine | filter parse/eval edge + Rust tests |
| `CosmWasm/cosmwasm` | 1144 | silent | Wasm smart-contract platform (Cosmos) | contract/API/path edge + Rust tests |
| `qmonnet/rbpf` | 1127 | silent | Rust eBPF VM + JIT | eBPF decode/JIT edge + Rust tests |
| `bytecodealliance/wizer` | 1099 | disclosure | Wasm pre-initializer (BA AI policy) | wasm pre-init/path edge + tests — BA human-in-loop |

### Tier notes

**Best first homes (wasm / small languages / compiler cache):** `wasmi-labs/wasmi`, `bytecodealliance/javy`/`wizer`/`wit-bindgen` (BA human-in-loop), `ccache/ccache`, `janet-lang/janet`, `d5/tengo`, `saghul/txiki.js`, `pocketpy/pocketpy`, `containers/crun`, `asmjit/asmjit`, `trunk-rs/trunk`. One home at a time; copy that repo’s merged outsider PR voice. **BA:** no autonomous GitHub agents; human owns every line.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `matz/streem` | 4597 | silent | Prototype stream language — not shipping product queue |
| `openxla/xla` | 4522 | silent | ML compiler mega-repo — prefer smaller language/wasm homes |
| `lotabout/write-a-C-interpreter` | 4401 | silent | Tutorial C interpreter (c4-inspired) — teaching not product |
| `zenc-lang/zenc` | 4310 | silent | Niche/young language; weak outsider process signal |
| `iree-org/iree` | 3923 | silent | MLIR ML compiler/runtime — ML-compiler farm, weak playbook hunk class |
| `facebookincubator/MetaPython` | 3792 | silent | Meta CPython fork — heavy process / wrong outsider home |
| `microsoft/verona` | 3726 | silent | Research concurrent ownership language — not product queue |
| `NerdLang/nerd` | 3613 | silent | Experimental JS-without-VM project — weak product contrib fit |
| `aws/aws-lambda-rust-runtime` | 3613 | silent | Lambda glue runtime — not compiler/language product |
| `krustlet/krustlet` | 3598 | silent | Kubernetes Rust Kubelet — archived/quiet; wrong class |
| `quickjs-zh/QuickJS` | 3514 | silent | Chinese QuickJS fork/mirror — prefer upstream QuickJS culture |
| `flaneur2020/pua-lang` | 3310 | silent | Meme/joke Monkey dialect — not product |
| `anthropics/claudes-c-compiler` | 2784 | silent | LLM demo C compiler novelty — not product queue |
| `rust-lang/rustc_codegen_cranelift` | 2135 | hostility_risk | rustc backend — forge mentor-gated LLM posture; leave for new-account drive-by |
| `nasa/spacewasm` | 1552 | hostility_risk | AI_POLICY generally disallows generative AI for interpreter src/* — leave |
| `rust-lang/rustc_codegen_gcc` | 1162 | hostility_risk | rustc backend — forge mentor-gated LLM posture; leave for new-account drive-by |

## Sector synthesis

- Midband (1k-5k) deep sample: **79** curated product repos.
- Proceed **63** / Leave **16**.
- Disclosure repos: `bytecodealliance/javy`, `bytecodealliance/wit-bindgen`, `bytecodealliance/wizer`.
- Hostility/mentor-gated: `rust-lang/rustc_codegen_cranelift`, `nasa/spacewasm`, `rust-lang/rustc_codegen_gcc`.
- No AgentScan adopter/org hits inside this midband sample (local blacklist checked). Re-run `--refresh` before any future fork.
- Method: policy files via `raw.githubusercontent.com` (CONTRIBUTING*/AI*/AGENTS*/PR templates/SECURITY); `gh api` workflows when needed; local AgentScan blacklist.
- No fork / PR / tracker comment performed.

## Deepen pass (2026-09-09, +44 scored)

Account: `vulragrag-star` · Curated product midband leftovers — linkers, language VMs, assemblers/disassemblers, small compilers, Starlark/CEL/Nickel/KCL surfaces · Policy via `raw.githubusercontent.com` · **31** proceed / **13** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'disclosure': 3, 'silent': 39, 'hard_ban': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `zrax/pycdc` | 4611 | silent | C++ Python bytecode disassembler/decompiler product | pyc decode/path edge + C++ tests |
| `zyantific/zydis` | 4360 | silent | Fast x86/x86-64 disassembler + code generation library | decode/encode API or path edge + C tests |
| `wild-linker/wild` | 3955 | disclosure | Very fast Linux linker (lld-class); human-in-loop AI ownership in CONTRIBUTING | linker path/argv/reloc edge + Rust tests — disclose/human-owns |
| `icedland/iced` | 3561 | silent | x86/x64 disassembler/assembler/decoder/encoder (Rust/.NET/Java/Python) | instruction decode/encode edge + Rust tests |
| `NVlabs/cuda-oxide` | 3132 | silent | Experimental Rust→CUDA SIMT compiler | kernel codegen/path edge + Rust tests |
| `cel-expr/cel-go` | 3092 | silent | CEL expression language evaluator (Go); gradual typing | CEL parse/eval edge + Go tests |
| `chaosprint/glicol` | 2995 | silent | Graph-oriented live-coding audio language + DSP lib | Glicol parse/graph edge + Rust tests |
| `nickel-lang/nickel` | 2993 | silent | Nickel configuration language (typed contracts) | Nickel parse/typecheck/path edge + Rust tests |
| `mstorsjo/llvm-mingw` | 2949 | silent | LLVM/Clang/LLD mingw-w64 cross toolchain product | toolchain path/target/sysroot edge + shell/C tests |
| `google/starlark-go` | 2758 | silent | Starlark configuration language implemented in Go | Starlark parse/eval edge + Go tests |
| `kaleidawave/ezno` | 2733 | silent | TypeScript type checker/compiler experiments | TS check/parse edge + Rust tests |
| `cc65/cc65` | 2687 | silent | Freeware C compiler for 6502-based systems | compile/link/path edge + C tests |
| `marcj/TypeRunner` | 2656 | silent | High-performance TypeScript compiler (C++) | TS parse/emit path edge + C++ tests |
| `vnmakarov/mir` | 2650 | silent | Lightweight MIR JIT + C11 JIT interpreter | MIR JIT/API edge + C tests |
| `keystone-engine/keystone` | 2633 | silent | Multi-arch assembler framework (Arm/x86/…) | assemble API/arch edge + C++ tests |
| `drh/lcc` | 2618 | silent | Classic retargetable ANSI C compiler | compile/target/path edge + C tests |
| `seanbaxter/circle` | 2576 | silent | Circle C++ compiler product surface | Circle compile/path edge + tests |
| `mattwparas/steel` | 2571 | silent | Embedded Scheme interpreter in Rust | Scheme parse/eval edge + Rust tests |
| `thepowersgang/mrustc` | 2524 | silent | Alternative Rust compiler reimplementation | Rust parse/lowering edge + C++ tests |
| `mthom/scryer-prolog` | 2452 | silent | Modern Prolog implementation mostly in Rust | Prolog parse/ISO edge + Rust tests |
| `kcl-lang/kcl` | 2408 | silent | KCL configuration programming language core (CNCF sandbox) | KCL parse/typecheck/path edge + Rust tests |
| `AcademySoftwareFoundation/OpenShadingLanguage` | 2332 | disclosure | Production GI shading language; ASWF AI disclosure/AGENTS policy | OSL parse/shader edge + C++ tests — follow ASWF disclosure |
| `rune-rs/rune` | 2321 | silent | Embeddable dynamic programming language for Rust | Rune parse/VM edge + Rust tests |
| `gbdk-2020/gbdk-2020` | 2294 | silent | Updated GBDK: C compiler/assembler/linker for Game Boy | compile/link/path edge + C tests |
| `herumi/xbyak` | 2271 | silent | JIT assembler for x86/x64 with modern ISAs | JIT emit/API edge + C++ tests |
| `nature-lang/nature` | 2252 | silent | Nature programming language compiler/runtime | parser/codegen/path edge + C tests |
| `Storyyeller/Krakatau` | 2248 | silent | Java decompiler, assembler, and disassembler | classfile decode/assemble edge + Rust tests |
| `uiua-lang/uiua` | 2162 | silent | Tacit array programming language | Uiua parse/array edge + Rust tests |
| `wasmerio/wasmer-python` | 2151 | silent | Wasmer WebAssembly runtime bindings for Python | wasm load/host API edge + Python/Rust tests |
| `kyren/piccolo` | 2149 | silent | Stackless Lua VM in pure Rust | Lua bytecode/VM edge + Rust tests |
| `aurae-runtime/aurae` | 1911 | silent | Distributed systems runtime daemon (Rust) | runtime API/path/config edge + Rust tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `rivet-dev/agentos` | 4608 | silent | Agent OS library — agent-sandbox adjacency, not compiler/runtime farm |
| `geohot/qira` | 4070 | silent | QEMU Interactive Runtime Analyser — QEMU-adjacent analysis tool; prefer leave |
| `banach-space/llvm-tutor` | 3435 | silent | Teaching out-of-tree LLVM passes — tutorial, not product farm |
| `emojicode/emojicode` | 3414 | silent | Emoji novelty language — weak product contrib fit for atlas farm |
| `google-ai-edge/LiteRT` | 3380 | silent | On-device ML runtime (TFLite successor) — ML mega, not language/wasm home |
| `jfecher/ante` | 2337 | hard_ban | CONTRIBUTING NO-AI / hard ban on AI contributions — leave |
| `boxlite-ai/boxlite` | 2305 | hard_ban | PR template NO-AI phrase — hard leave; also agent micro-VM adjacency |
| `llvm/circt` | 2237 | disclosure | Circuit IR Compilers (MLIR) — large LLVM subproject / heavy process for first home |
| `spencertipping/jit-tutorial` | 1934 | silent | How-to JIT tutorial — teaching artifact, not shipping product |
| `llvm/torch-mlir` | 1907 | silent | PyTorch↔MLIR bridge — ML-compiler mega surface, weak playbook hunk class |
| `diekmann/wasm-fizzbuzz` | 1557 | silent | Wasm-from-scratch tutorial (FizzBuzz→Doom) — teaching not product |
| `wa-lang/ugo-compiler-book` | 1537 | silent | µGo compiler book/code — teaching, not product queue |
| `Spu7Nix/SPWN-language` | 1183 | silent | Geometry Dash trigger language — niche game DSL, weak outsider process |

Notes: Prefer small language/wasm/linker/assembler homes with regression tests. Leave teaching books, ML mega-compilers (Torch-MLIR/LiteRT), emoji/game DSLs, QEMU-adjacent analysers, agent OS/micro-VM novelty, and hard NO-AI repos (`jfecher/ante`, `boxlite-ai/boxlite`). `wild-linker/wild` and ASWF OSL need human-owned disclosure.

## Product deepen midband subset (2026-09-11, +34 scored)

Account: `vulragrag-star` · Curated compiler/runtime/Wasm/language product homes still missing after midband + famous-CLI passes · Policy via `raw.githubusercontent.com` · **23** proceed / **11** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 32, 'disclosure': 1, 'hostility_risk': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `mozilla/rhino` | 4625 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `babashka/babashka` | 4605 | silent | babashka language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `adafruit/circuitpython` | 4553 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `dhall-lang/dhall-lang` | 4484 | silent | Config/data language; parse/eval edges | parse/eval/path edge + tests |
| `dotnet/fsharp` | 4331 | silent | fsharp language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `just-js/just` | 3806 | silent | just language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `quickjs-ng/quickjs` | 3731 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `grain-lang/grain` | 3466 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `dlang/dmd` | 3307 | silent | dmd language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `fibjs/fibjs` | 3097 | silent | fibjs language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `TheDan64/inkwell` | 3013 | silent | Runtime/bindings product surface; config/path edges | config/path/API edge + tests |
| `mlua-rs/mlua` | 2861 | silent | Runtime/bindings product surface; config/path edges | config/path/API edge + tests |
| `sharkdp/numbat` | 2684 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `lfe/lfe` | 2455 | silent | lfe language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `thheller/shadow-cljs` | 2407 | silent | shadow-cljs language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `mun-lang/mun` | 2132 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `vtereshkov/umka-lang` | 2103 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `pypy/pypy` | 1793 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `bytecodealliance/wasm-tools` | 1789 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `WebAssembly/wasi-sdk` | 1636 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `Moddable-OpenSource/moddable` | 1552 | silent | moddable language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `babashka/sci` | 1383 | silent | sci language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `ldc-developers/ldc` | 1371 | silent | ldc language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `hyperlight-dev/hyperlight` | 4675 | silent | Agent-oriented lightweight VMM — leave agent infrastructure |
| `ballercat/walt` | 4630 | silent | Walt JS→Wasm syntax — stale/niche; leave |
| `WebAssembly/spec` | 3450 | silent | WASM specification / reference interpreter — not product CLI farm |
| `ghc/ghc` | 3273 | silent | GHC mirror; Haskell core process — leave |
| `idris-lang/Idris2` | 3060 | disclosure | Dependently typed language / proof orbit — leave |
| `agda/agda` | 2930 | silent | Dependently typed proof assistant — leave |
| `Perl/perl5` | 2325 | hostility_risk | AI_POLICY mentor-gated LLM + human-ownership — leave |
| `bluealloy/revm` | 2231 | silent | Ethereum VM — blockchain runtime; leave chain farm |
| `cesanta/mjs` | 2055 | silent | Tiny embedded JS; sparse tests/community — leave |
| `factor/factor` | 1849 | silent | Factor image-based language; high onboarding friction — leave |
| `pharo-project/pharo` | 1484 | silent | Pharo Smalltalk image workflow — leave |

Notes: Prefer midband embeddable/scripting (umka/mun/numbat/mlua/inkwell/babashka/sci/shadow-cljs/lfe). Leave proof assistants, Factor/Pharo image workflows, stale Walt, and chain EVMs.

## Midband product deepen (2026-09-12, +71 scored)

Account: `vulragrag-star` · Curated compilers-runtimes midband (1k–5k★) product language/Wasm/JIT/interpreter/assembler/emulator/shader/HDL toolchain homes still missing after prior compilers-runtimes midband deepen · Policy via `raw.githubusercontent.com` · **54** proceed / **17** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 65, 'disclosure': 6}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `google/wuffs` | 4823 | silent | Memory-safe untrusted file-format codecs / transpiler | wuffs transpile/decode edge + Go/C tests |
| `immunant/c2rust` | 4800 | silent | C-to-Rust transpiler / migration toolchain | transpile AST/path edge + Rust tests |
| `86Box/86Box` | 4790 | disclosure | x86 PC machine emulator (disclosure CoC); BIOS/device/path edges | device/BIOS/path edge + C tests — disclose AI |
| `chipsalliance/chisel` | 4779 | disclosure | Modern hardware design language on Scala (disclosure PR template) | HDL elaborat/FIRRTL edge + Scala tests — disclose AI |
| `YosysHQ/yosys` | 4748 | silent | Open synthesis suite (Verilog→netlist) product CLI | synth pass/path edge + C++ tests |
| `scala-js/scala-js` | 4710 | silent | Scala-to-JavaScript compiler product | Scala.js codegen/IR edge + Scala tests |
| `kaitai-io/kaitai_struct` | 4673 | silent | Declarative binary format → parser codegen | kaitai compile/path edge + multi-lang tests |
| `libffi/libffi` | 4365 | silent | Portable foreign-function interface library | FFI ABI/calling-conv edge + C tests |
| `evhub/coconut` | 4355 | silent | Coconut functional Python → Python compiler | Coconut transpile/path edge + Python tests |
| `jruby/jruby` | 3916 | silent | Ruby on the JVM; runtime/IR/path edges | Ruby JVM runtime/IR edge + Ruby tests |
| `ptitSeb/box86` | 3802 | silent | Linux userspace x86 emulator on ARM; dynarec/path edges | dynarec/path/ELF edge + C tests |
| `kach/nearley` | 3742 | silent | JS parser toolkit (Earley); grammar/compile edges | grammar/compile edge + JS tests |
| `joncampbell123/dosbox-x` | 3720 | silent | DOSBox-X PC/DOS emulator product; config/device/path edges | DOS device/config/path edge + C++ tests |
| `steveicarus/iverilog` | 3632 | silent | Icarus Verilog simulator/compiler | Verilog parse/sim edge + C++ tests |
| `momo5502/sogen` | 3612 | silent | Windows/Linux userspace emulator; syscall/PE/path edges | syscall/PE/path edge + C++ tests |
| `KhronosGroup/glslang` | 3581 | disclosure | Khronos GLSL/ESSL front-end + SPIR-V (disclosure AI policy) | GLSL parse/SPIR-V edge + C++ tests — disclose AI |
| `eclipse-openj9/openj9` | 3545 | disclosure | Eclipse OpenJ9 JVM (disclosure AI policy); JIT/GC/path edges | JVM JIT/GC/path edge + C++ tests — disclose AI |
| `lalrpop/lalrpop` | 3504 | silent | LR(1) parser generator for Rust | grammar/codegen edge + Rust tests |
| `mortbopet/Ripes` | 3417 | silent | Graphical RISC-V processor simulator + assembly editor | Ripes asm/sim edge + C++ tests |
| `netwide-assembler/nasm` | 3311 | silent | NASM x86 assembler product CLI | asm parse/encode/path edge + C tests |
| `riscv-software-src/riscv-isa-sim` | 3226 | silent | Spike RISC-V ISA simulator; CSR/trap/path edges | RISC-V CSR/trap edge + C++ tests |
| `truffleruby/truffleruby` | 3221 | silent | High-performance Ruby on GraalVM Truffle | Truffle Ruby runtime edge + Ruby tests |
| `DynamoRIO/dynamorio` | 3160 | disclosure | Dynamic binary instrumentation platform (disclosure AI policy) | DBI client/trace edge + C tests — disclose AI |
| `ingokegel/jclasslib` | 2997 | silent | Java bytecode viewer/editor product | classfile parse/edit edge + Kotlin tests |
| `ghdl/ghdl` | 2889 | silent | VHDL 2008/93/87 simulator/analyzer | VHDL analyze/sim edge + Ada/C tests |
| `teal-language/tl` | 2820 | silent | Teal typed-Lua compiler product | Teal typecheck/codegen edge + Lua tests |
| `Chevrotain/chevrotain` | 2801 | silent | JS parser-building toolkit | lexer/parser API edge + TS tests |
| `IronLanguages/ironpython3` | 2760 | silent | Python 3 on .NET; runtime/interop edges | IronPython runtime/interop edge + C# tests |
| `TypeScriptToLua/TypeScriptToLua` | 2542 | silent | TypeScript→Lua transpiler product | TS→Lua emit/path edge + TS tests |
| `KhronosGroup/SPIRV-Cross` | 2511 | silent | SPIR-V → GLSL/HLSL/MSL reflection/compiler tool | SPIR-V cross-compile edge + C++ tests |
| `wasmCloud/wasmCloud` | 2436 | silent | CNCF Wasm application runtime / host | wasm host/capability edge + Rust tests |
| `edubart/nelua-lang` | 2420 | silent | Minimal statically-typed systems language → C/LuaJIT | Nelua compile/path edge + Lua tests |
| `google/gnostic` | 2300 | silent | OpenAPI → compiler/codegen toolkit | OpenAPI compile/path edge + Go tests |
| `cosmos72/gomacro` | 2300 | silent | Interactive Go interpreter/REPL with eval | Go interpret/eval edge + Go tests |
| `google/shaderc` | 2181 | silent | Vulkan shader compile tools (glslc) collection | shaderc CLI/path edge + C++ tests |
| `cnlohr/mini-rv32ima` | 2174 | silent | Tiny header-only RISC-V emulator | RISC-V emu/instr edge + C tests |
| `serge-sans-paille/pythran` | 2142 | silent | AOT compiler for numeric Python kernels | Pythran AOT/path edge + Python tests |
| `benhoyt/goawk` | 2053 | silent | POSIX AWK interpreter in Go (+ CSV mode) | AWK parse/runtime edge + Go tests |
| `SpinalHDL/SpinalHDL` | 2038 | silent | Scala-based HDL generator product | Spinal elaborat/Verilog edge + Scala tests |
| `oracle/graaljs` | 2026 | silent | GraalJS ECMAScript runtime on GraalVM | JS runtime/interop edge + Java tests |
| `blend2d/blend2d` | 1986 | silent | 2D vector graphics engine with JIT compiler | JIT pipeline/path edge + C++ tests |
| `AdaptiveCpp/AdaptiveCpp` | 1934 | silent | SYCL/C++ parallel compiler (hipSYCL lineage) | SYCL compile/target edge + C++ tests |
| `google/xls` | 1882 | silent | XLS accelerated hardware synthesis (DSL→RTL) | XLS IR/codegen edge + C++ tests |
| `lifting-bits/remill` | 1825 | silent | Lift machine code → LLVM bitcode library | lifter decode/LLVM edge + C++ tests |
| `oracle/graalpython` | 1642 | silent | GraalPy embeddable Python 3 on GraalVM | Python runtime/interop edge + Java tests |
| `intelxed/xed` | 1615 | silent | Intel XED x86 encoder/decoder library | x86 encode/decode API edge + C tests |
| `clash-lang/clash-compiler` | 1612 | silent | Haskell → VHDL/Verilog/SystemVerilog compiler | Clash HDL emit edge + Haskell tests |
| `jython/jython` | 1540 | silent | Python on the JVM implementation | Jython runtime/path edge + Java tests |
| `yasm/yasm` | 1482 | silent | Yasm modular assembler (NASM/GAS syntax) | asm parse/encode edge + C tests |
| `bochs-emu/Bochs` | 1361 | silent | Bochs IA-32 PC emulator | PC emu/device/path edge + C++ tests |
| `KhronosGroup/SPIRV-Tools` | 1357 | silent | SPIR-V optimizer/validator/assembler tools | SPIR-V opt/validate edge + C++ tests |
| `B-Lang-org/bsc` | 1143 | silent | Bluespec SystemVerilog compiler | BSC compile/sim edge + Haskell tests |
| `myhdl/myhdl` | 1128 | silent | Python HDL → Verilog/VHDL conversion | MyHDL convert/path edge + Python tests |
| `veryl-lang/veryl` | 1034 | disclosure | Modern HDL (disclosure AI policy); compile/emit edges | Veryl parse/emit edge + Rust tests — disclose AI |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `pegjs/pegjs` | 4903 | silent | Legacy PEG.js (largely superseded / low maintainer energy for agent PRs) |
| `vercel-labs/scriptc` | 4817 | silent | Vercel Labs TypeScript-to-native novelty compiler — not stable product home |
| `JonathanSalwan/Triton` | 4291 | silent | DBA/symbolic RE framework — security-crypto sector spill |
| `mint-lang/mint` | 4267 | silent | Front-end novelty language — thin product/regression surface |
| `cea-sec/miasm` | 3960 | silent | Reverse-engineering framework — security-crypto sector spill |
| `skulpt/skulpt` | 3399 | silent | In-browser Python teaching runtime — tutorial/demo surface |
| `plasma-disassembler/plasma` | 3069 | silent | Interactive disassembler — security/RE spill, thin CR product lens |
| `weld-project/weld` | 3006 | silent | Analytics runtime (Stanford Weld) — ML/data mega-compiler adjacency, quiet |
| `d4l3k/go-pry` | 3004 | silent | Go REPL novelty — not a compiler/runtime product farm |
| `bytenode/bytenode` | 2975 | silent | Node bytecode packer utility — packaging trick, not language product |
| `TranscryptOrg/Transcrypt` | 2919 | silent | Python→JS teaching transpiler — weak regression/product surface |
| `google/cpu_features` | 2618 | silent | Tiny CPU feature-detect library — not a compiler/runtime product |
| `AbsInt/CompCert` | 2224 | silent | Formally-verified C compiler — academic/proof-hostile contribution climate |
| `codeplea/tinyexpr` | 1924 | silent | Tiny expression evaluator — toy/lib, not toolchain product |
| `cesanta/elk` | 1900 | silent | Ultra-low-footprint embedded JS toy engine |
| `moonbitlang/core` | 1204 | silent | MoonBit stdlib satellite — language compiler home not midband-scored here |
| `node-ffi-napi/node-ffi-napi` | 1095 | silent | Legacy Node FFI binding — stale vs napi-rs/cxx; weak farm |

Notes: Prefer midband product compilers/runtimes (languages, Wasm/JIT VMs, interpreters, assembler/disassembler, userspace CPU emulators, shader/HDL toolchains, binding generators). Disclosure: cosmopolitan/box64/86Box/chisel/glslang/openj9/dynamorio/slang/veryl. Hard leave: capstone (forbids AI), FEX-Emu (NO-AI). Leave browser-Python toys (brython/skulpt), Vercel Labs scriptc, mint-lang novelty, RE frameworks (Triton/miasm/plasma), CompCert academic, tinyexpr/elk toys, MoonBit core satellite, node-ffi-napi, cpu_features lib.

