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

