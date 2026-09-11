# Sector survey: compilers-runtimes

Account: `vulragrag-star` · refreshed `2026-09-08T17:38:01Z` · TS/JS/Zig DevEx slice · No fork/PR/comment.

Playbook lens: parser/path/formatter/LSP/bundler tooling with tests.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 123 | No hard ban in common paths |
| disclosure | 10 | AI disclosure language |
| hard_ban | 1 | Hard AI ban |
| agentscan | 2 | AgentScan |
| hostility_risk | 4 | Hostility-adjacent |

Proceed: **94** · Leave: **46**.

## PROCEED candidates (contrib fit)

| Repo | Stars | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `microsoft/TypeScript` | 110981 | disclosure | TypeScript compiler; parse/check edges - CONTRIBUTING disclosure | TS parse/check/path edge + tests - disclose AI assist |
| `oven-sh/bun` | 95915 | silent | JS/TS runtime; no hard AI ban; product code with tests | runtime CLI/path/Node-compat edge + tests |
| `FuelLabs/sway` | 61454 | silent | Sway language compiler; prefer parser over chain farm | parser/typecheck edge + tests |
| `bytecodealliance/wasmtime` | 18607 | disclosure | BA AI policy (LLVM-derived): human-in-loop; **no AI on GFI**; no agent-opened PRs | wasm/WASI/CLI path edge + tests |
| `tinygo-org/tinygo` | 17707 | silent | Go compiler for WASM/MCU; silent policy | target/linker/wasm export edge + tests |
| `rust-lang/rust-analyzer` | 16825 | disclosure | Disclose AI; no autonomous agents; **no AI on E-easy**; human review replies | analysis/IDE edge + tests — avoid E-easy |
| `openresty/openresty` | 14028 | silent | Nginx+LuaJIT platform; product packaging/path edges | build/path/LuaJIT packaging edge + tests |
| `gopherjs/gopherjs` | 13183 | silent | Go→JS compiler | compiler/js-runtime edge + tests |
| `foundry-rs/foundry` | 10583 | disclosure | Must disclose AI assistance extent in PR | CLI flag/path/tool edge + tests |
| `wasm-bindgen/wasm-bindgen` | 9145 | silent | Rust↔Wasm interop; attr/parser edges | bindgen attribute/path parse edge + tests |
| `awslabs/llrt` | 8801 | silent | Lightweight experimental JS runtime | runtime API/compat edge + tests |
| `cloudflare/workerd` | 8696 | silent | Workers JS/Wasm runtime; AGENTS.md assistant guide ≠ ban | compat/flag/isolate edge + tests |
| `avast/retdec` | 8623 | silent | LLVM-based retargetable decompiler | decoder/path edge + tests |
| `robertkrimen/otto` | 8449 | silent | JS interpreter in Go; small surface | parser/eval edge + tests |
| `traefik/yaegi` | 8391 | silent | Elegant Go interpreter | interp/import path edge + tests |
| `pydantic/monty` | 8184 | silent | Minimal secure Python interpreter (Rust) | parser/runtime edge + tests |
| `expr-lang/expr` | 8003 | silent | Go expression language | expr parse/eval edge + tests |
| `napi-rs/napi-rs` | 7934 | silent | Node native addon framework; FFI/build/path edges | N-API build/path edge + tests |
| `parcel-bundler/lightningcss` | 7674 | silent | CSS parser/bundler/minifier with fixtures | CSS parse/minify fixture edge + tests |
| `youki-dev/youki` | 7593 | silent | OCI container runtime (Rust) | runtime config/path edge + tests |
| `boa-dev/boa` | 7538 | silent | Embeddable JS engine (Rust) | parser/VM edge + tests |
| `jerryscript-project/jerryscript` | 7417 | silent | Ultra-light JS engine (C) | parser/API edge + tests |
| `yuin/gopher-lua` | 6979 | silent | Lua VM+compiler in Go | VM/compiler parse edge + tests |
| `halide/Halide` | 6598 | disclosure | LLVM-adjacent; Co-authored-by required for significant AI | schedule/codegen/path edge + tests |
| `facebook/redex` | 6300 | silent | Android bytecode optimizer | bytecode pass/path edge + tests |
| `wasm-micro-runtime/wasm-micro-runtime` | 6085 | silent | WAMR; AI size guidance in CONTRIBUTING — human owns PR | AOT/interpreter/config path edge + tests |
| `extism/extism` | 5756 | silent | Wasm plugin framework | host/PDK path edge + tests |
| `rhaiscript/rhai` | 5661 | silent | Embedded scripting for Rust | script parser/engine edge + tests |
| `amber-lang/amber` | 5220 | silent | Lang → Bash/Ksh compiler | parser/shell-codegen edge + tests |
| `monoio-rs/monoio` | 5106 | silent | io-uring async runtime | runtime/io edge + tests |
| `smol-rs/smol` | 5060 | silent | Small/fast Rust async runtime | runtime spawn/path edge + tests |
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

## LEAVE list

| Repo | Stars | Policy | Reason |
|---|---:|---|---|
| `vercel/next.js` | 142213 | silent | React framework — weak compilers-runtime hunk fit; docs/feature farm risk |
| `rust-lang/rust` | 117990 | disclosure | Forge LLM policy: LLM-created code only with pre-arranged mentor + llm-assisted; leave for new-account drive-by |
| `denoland/deno` | 108395 | disclosure | Predecessor open queue (CATALOG) — do not steal |
| `sveltejs/svelte` | 88103 | agentscan | bluwy / AgentScan extra_orgs — leave circle |
| `protocolbuffers/protobuf` | 72007 | silent | Serialization mega-repo — prefer dedicated runtimes |
| `daytonaio/daytona` | 71764 | silent | AI sandbox infra — wrong class / agent-platform farm |
| `openinterpreter/openinterpreter` | 68269 | silent | Coding-agent product — not compiler/runtime contrib home |
| `webpack/webpack` | 65964 | silent | Bundler farm; prefer language/wasm/JIT runtimes |
| `gatsbyjs/gatsby` | 55940 | silent | React framework — wrong class |
| `typst/typst` | 55907 | hard_ban | CONTRIBUTING forbids AI-implemented contributions and AI PR descriptions |
| `JetBrains/kotlin` | 53377 | silent | Language mega-repo; JetBrains process heavy |
| `skylot/jadx` | 50375 | silent | Decompiler UI — weak quoting/path playbook class |
| `RPCS3/rpcs3` | 19686 | silent | Emulator — wrong class for playbook hunks |
| `kitao/pyxel` | 17827 | silent | Retro game engine — wrong class |
| `opensandbox-group/OpenSandbox` | 15035 | silent | AI-agent sandbox runtime — wrong class for playbook |
| `DoctorWkt/acwj` | 13406 | silent | Tutorial 'Compiler Writing Journey' — teaching not product |
| `web-infra-dev/rspack` | 12892 | silent | Bundler — prefer runtimes |
| `rui314/chibicc` | 11876 | silent | Teaching C compiler — not product queue |
| `johnthagen/min-sized-rust` | 9850 | silent | Docs/guide repo — not product code |
| `bytedance/sonic` | 9597 | silent | JSON serde — not compiler/runtime core |
| `love2d/love` | 8686 | silent | Game framework — wrong class |
| `AFLplusplus/AFLplusplus` | 6749 | silent | Fuzzer / QEMU-adjacent — security drive-by risk |
| `rust-lang/miri` | 6566 | hostility_risk | LLM PR code only with prior Miri mentor agreement |
| `rui314/8cc` | 6416 | silent | Teaching C compiler |
| `hsutter/cppfront` | 6001 | silent | Personal experimental compiler |
| `voidzero-dev/vite-plus` | 5746 | agentscan | voidzero-dev AgentScan circle |
| `lemonade-sdk/lemonade` | 5658 | silent | Local AI app runner — wrong class |
| `farm-fe/farm` | 5590 | silent | Vite-like bundler — lower priority |
| `EsotericSoftware/spine-runtimes` | 5286 | silent | Animation runtimes — wrong class |
| `zpoint/CPython-Internals` | 5077 | silent | Internals notes / docs — not contrib product |
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

- Refreshed after TS/JS/Zig DevEx product slice.
- No tracker comments/forks/third-party PRs.
- scored_at: `2026-09-08T17:38:01Z`

## Product deepen (≥5k★ subset) (2026-09-11, +69 scored)

Account: `vulragrag-star` · Curated compiler/runtime/Wasm/language product homes still missing after midband + famous-CLI passes · Policy via `raw.githubusercontent.com` · **41** proceed / **28** leave · No fork/PR/comment.

Policy histogram (this pass): `{'disclosure': 11, 'silent': 53, 'agentscan': 1, 'hard_ban': 4}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `JuliaLang/julia` | 49089 | disclosure | Julia language; parse/runtime edges — disclose AI assist | parse/runtime/path edge + tests — disclose AI |
| `vlang/v` | 37842 | silent | v language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `emscripten-core/emscripten` | 27607 | silent | emscripten language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `elixir-lang/elixir` | 26629 | disclosure | Elixir language; compile/macro path — disclose AI | compile/macro/path edge + tests — disclose AI |
| `RustPython/RustPython` | 22344 | disclosure | Python interpreter in Rust — disclose AI policy | parser/runtime/path edge + Rust tests — disclose AI |
| `micropython/micropython` | 22054 | disclosure | MCU Python; port/path edges — AI policy disclosure | port/path/API edge + C tests — disclose AI |
| `gleam-lang/gleam` | 21896 | silent | gleam language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `wasmerio/wasmer` | 21025 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `crystal-lang/crystal` | 20402 | silent | crystal language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `wenyan-lang/wenyan` | 20268 | silent | wenyan language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `nim-lang/Nim` | 18232 | silent | Nim language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `AssemblyScript/assemblyscript` | 18013 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `erlang/otp` | 12330 | silent | otp language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `odin-lang/Odin` | 11894 | silent | Odin language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `facebook/hermes` | 11302 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `dart-lang/sdk` | 11278 | disclosure | Dart SDK/VM/compilers — disclose AI | VM/compiler/path edge + tests — disclose AI |
| `bellard/quickjs` | 10983 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `clojure/clojure` | 10955 | silent | clojure language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `cython/cython` | 10843 | silent | Language/compiler product; parse/codegen edges | parser/codegen/path edge + tests |
| `WasmEdge/WasmEdge` | 10799 | disclosure | Wasm runtime; plugin/path — disclose AI | runtime/plugin/path edge + tests — disclose AI |
| `goplus/xgo` | 9458 | silent | xgo language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `clojure/clojurescript` | 9391 | silent | clojurescript language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `purescript/purescript` | 8909 | silent | purescript language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `WebAssembly/binaryen` | 8622 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `wren-lang/wren` | 8128 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `WebAssembly/wabt` | 8124 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `wasm3/wasm3` | 8025 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `elm/compiler` | 7900 | silent | compiler language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `google/jsonnet` | 7566 | silent | Config/data language; parse/eval edges | parse/eval/path edge + tests |
| `rescript-lang/rescript` | 7443 | silent | rescript language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `wasm-bindgen/wasm-pack` | 7283 | silent | Wasm toolchain/runtime product; module/path/CLI edges | wasm module/path/CLI edge + tests |
| `HaxeFoundation/haxe` | 6926 | silent | haxe language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `ocaml/ocaml` | 6553 | disclosure | OCaml compiler/runtime — AI.md disclosure/HITL | parse/typecheck/path edge + tests — disclose AI |
| `imba/imba` | 6508 | silent | imba language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `spinframework/spin` | 6508 | silent | Runtime/bindings product surface; config/path edges | config/path/API edge + tests |
| `cue-lang/cue` | 6249 | silent | Config/data language; parse/eval edges | parse/eval/path edge + tests |
| `bellard/mquickjs` | 6159 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `roc-lang/roc` | 6040 | silent | roc language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |
| `luau-lang/luau` | 5855 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `LuaJIT/LuaJIT` | 5763 | silent | Embeddable JS/Lua engine; parse/eval/path edges | parser/eval/path edge + tests |
| `racket/racket` | 5207 | silent | racket language/runtime product; parser/path/CLI edges | parser/runtime/path edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `golang/go` | 138403 | silent | Go core; proposal/Gerrit culture — leave core; prefer tooling satellites already scored |
| `nodejs/node` | 121574 | agentscan | AgentScan adopter — leave the Node circle |
| `godotengine/godot` | 116947 | hard_ban | Godot autonomous-agent / vibe-coding auto-ban — hard leave |
| `swiftlang/swift` | 70336 | silent | Swift compiler mega; Apple contribution process — leave |
| `ziglang/zig` | 43306 | hard_ban | Playbook Zig no-LLM ban (issues/PRs/comments) — hard leave; zls separately proceed |
| `llvm/llvm-project` | 40412 | silent | LLVM monorepo mega; mentor/Phabricator-class process — leave |
| `php/php-src` | 40368 | silent | PHP core; RFC/karma culture — leave |
| `carbon-language/carbon-lang` | 33887 | disclosure | Google experimental language; CLA/process heavy — leave for now |
| `argotorg/solidity` | 25735 | hard_ban | PR template NO-AI — hard leave |
| `v8/v8` | 25238 | silent | V8 engine mirror; Chromium process — leave |
| `ruby/ruby` | 23720 | silent | Ruby core; mature committer culture — leave |
| `copy/v86` | 23471 | silent | x86-in-browser emulator — leave full emulator class |
| `openjdk/jdk` | 23336 | hard_ban | OpenJDK GB interim: no LLM content in git/PRs/mail — hard leave |
| `oracle/graal` | 21696 | disclosure | GraalVM mega; Oracle CLA/process — leave for outsider agent cadence |
| `dotnet/roslyn` | 20656 | silent | .NET compiler mega; Microsoft CLA/process — leave |
| `HigherOrderCO/Bend` | 19825 | silent | Research parallel language / HVM stack — leave research mega |
| `compiler-explorer/compiler-explorer` | 19059 | silent | Interactive compiler web app — leave mega frontend; prefer language homes |
| `facebook/hhvm` | 18661 | silent | HHVM/Hack mega — leave |
| `dotnet/runtime` | 18265 | silent | .NET runtime mega — leave |
| `leaningtech/webvm` | 17385 | silent | Browser VM demo product — leave emulator/demo surface |
| `gcc-mirror/gcc` | 11231 | silent | GCC mirror; GNU process / patch norms — leave |
| `chakra-core/ChakraCore` | 9255 | silent | Archived/legacy JS engine orbit — leave |
| `BoundaryML/baml` | 9165 | silent | Agent programming language product — not compiler hunk farm |
| `leanprover/lean4` | 9110 | disclosure | Theorem prover / mathlib orbit — leave proof-assistant farm |
| `scala/scala3` | 6299 | disclosure | Scala 3 compiler mega; SIP/process — leave core |
| `red/red` | 6037 | silent | Red language; sparse modern PR culture — leave |
| `WebAssembly/WASI` | 5793 | silent | WASI interface spec repo — prefer wasi-sdk/wasm-tools product surfaces |
| `rocq-prover/rocq` | 5571 | silent | Proof assistant mega (ex-Coq); leave theorem-prover farm |

Notes: Prefer Wasm toolchains/runtimes (wasmer/WasmEdge/wasm3/binaryen/wabt/wasm-tools/wasm-pack/AssemblyScript/spin), embeddable engines (quickjs/hermes/rhino/LuaJIT/luau/wren), and mid-size language homes (gleam/crystal/nim/elixir/julia/odin/v/grain/rescript/purescript/elm/cython/micropython/RustPython). Disclosure: Julia/elixir/RustPython/micropython/dart/WasmEdge/ocaml. Leave AgentScan nodejs, hard bans (zig/godot/OpenJDK/solidity), mentor-gated perl5, language megas (go/swift/llvm/gcc/php/ruby/v8/roslyn), proof assistants, agent langs (baml), emulators (v86/webvm).

