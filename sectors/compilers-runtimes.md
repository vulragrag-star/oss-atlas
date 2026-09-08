# Sector survey: compilers-runtimes

Account: `vulragrag-star` · Input: `survey/raw/compilers-runtimes.jsonl` (68 repos) · Deep-sampled **48** repos for AI/contrib policy via `gh api` + raw.githubusercontent (after core rate-limit) · Scored **60** lines · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **compiler/runtime/parser/path/build bugs with regression tests**. Prefer **LLVM-adjacent care (no AI on GFI)**, **language runtimes**, **wasm**, **JIT**. Leave hard bans + predecessor open queues.

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 49 | No hard ban in common CONTRIBUTING/AI paths |
| disclosure | 7 | BA/LLVM-style, rust-analyzer, PyO3, Halide Co-authored-by, Foundry disclose, Rust forge (leave) |
| hostility_risk | 1 | Miri mentor-gated LLM PRs |
| hard_ban | 1 | `typst/typst` forbids AI-implemented contributions |
| **agentscan** | 2 | `sveltejs/svelte`, `voidzero-dev/vite-plus` |

Proceed: **30** · Leave: **30** · Scored lines appended to `survey/scored.jsonl`. Notes: `survey/notes/compilers-runtimes-policy.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. **LLVM-adjacent / BA / rust-analyzer / PyO3: never use AI on good-first-issue / E-easy.**

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `oven-sh/bun` | 95915 | silent | JS/TS runtime; no hard AI ban; product code with tests | runtime CLI/path/Node-compat edge + tests |
| `FuelLabs/sway` | 61454 | silent | Sway language compiler; prefer parser over chain farm | parser/typecheck edge + tests |
| `bytecodealliance/wasmtime` | 18607 | disclosure | BA AI policy (LLVM-derived): human-in-loop; **no AI on GFI**; no agent-opened PRs | wasm/WASI/CLI path edge + tests |
| `tinygo-org/tinygo` | 17707 | silent | Go compiler for WASM/MCU; silent policy | target/linker/wasm export edge + tests |
| `rust-lang/rust-analyzer` | 16825 | disclosure | Disclose AI; no autonomous agents; **no AI on E-easy**; human review replies | analysis/IDE edge + tests — avoid E-easy |
| `PyO3/pyo3` | 16116 | disclosure | No unsolicited raw AI PRs; no AI on easy/GFI; disclose preferred | FFI/build/path edge + tests — avoid GFI |
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

### Tier notes

**Best first homes (wasm / JS engines / small interpreters):**

1. `bytecodealliance/wasmtime` — Wasmtime; follow [BA AI Tool Use Policy](https://github.com/bytecodealliance/governance/blob/main/AI_TOOL_POLICY.md) (LLVM-derived): human-in-loop, **no AI on GFI**, no autonomous GitHub agents.
2. `boa-dev/boa` / `jerryscript-project/jerryscript` / `robertkrimen/otto` — JS engines/interpreters with parser/VM edges + tests.
3. `tinygo-org/tinygo` / `wasm-bindgen/wasm-bindgen` / `wasm-micro-runtime/wasm-micro-runtime` / `extism/extism` — wasm toolchain/runtime band.
4. `oven-sh/bun` / `cloudflare/workerd` / `awslabs/llrt` — JS runtimes (Bun silent; workerd AGENTS.md is tooling guidance).
5. `traefik/yaegi` / `yuin/gopher-lua` / `expr-lang/expr` / `gopherjs/gopherjs` — Go interp/VM/compiler edges.
6. `pydantic/monty` / `rhaiscript/rhai` — embedded language runtimes in Rust.
7. `parcel-bundler/lightningcss` — CSS parser fixtures (closest “compiler” with playbook-shaped tests among bundlers).

**LLVM-adjacent care (disclose / trailers; no AI on GFI):**

- `halide/Halide` — Co-authored-by for significant AI.
- `avast/retdec` — LLVM decompiler; silent but treat like LLVM culture.
- `rust-lang/rust-analyzer` — AI_POLICY.md; **no AI on E-easy+E-has-instructions**; no autonomous agents; human review replies.
- `PyO3/pyo3` — no unsolicited raw AI PRs; no AI on easy/GFI; disclose preferred.

**Proceed with process friction:** `foundry-rs/foundry` (mandatory AI disclosure); `youki-dev/youki` (OCI runtime — path/config only); `FuelLabs/sway` / `amber-lang/amber` (language compilers — parser edges only); `facebook/redex` (Meta bytecode — CLA/process).

## LEAVE list

| Repo | ★ | Policy | Reason |
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

## Sector synthesis

- **Hard exclude:** `typst/typst` — CONTRIBUTING rejects AI-implemented contributions and AI-written PR descriptions. Do not argue on their tracker.
- **Mentor-gated (treat as leave for vulragrag-star cold start):** `rust-lang/rust` (forge LLM experiment needs pre-arranged reviewer + `llm-assisted`); `rust-lang/miri` (LLM PR code only with prior mentor).
- **Predecessor / AgentScan:** `denoland/deno` (open-queue steal); `sveltejs/svelte`, `voidzero-dev/vite-plus` (AgentScan circle).
- **Fit theme:** wasm runtimes (Wasmtime, WAMR, wasm-bindgen, Extism, TinyGo), JS engines/runtimes (Boa, JerryScript, Otto, Bun, workerd, LLRT), embedded langs (Rhai, Monty, Yaegi, gopher-lua, expr), LLVM-adj (Halide, RetDec) with GFI care.
- **Avoid:** frameworks/bundlers (`next.js`, `webpack`, `gatsby`, `rspack`, `farm`), teaching compilers (`chibicc`, `8cc`, `acwj`), emulators/games, AI-agent sandboxes (`daytona`, `OpenSandbox`, `openinterpreter`), docs dumps (`min-sized-rust`, `CPython-Internals`).
- **LLVM note:** BA policy explicitly copies LLVM AIToolPolicy — **no AI on good-first-issue**; extractive PRs get canned reply. Same discipline on rust-analyzer E-easy and PyO3 easy/GFI.

## Method notes

- Deep sample prioritized LLVM-adjacent, language runtimes, wasm, JIT from `survey/raw/compilers-runtimes.jsonl`.
- Policy files via `gh api` until core rate-limit; completed key live docs via `raw.githubusercontent.com` + forge/llvm.org HTML (Rust LLM policy, PyO3 contributing, BA `AI_TOOL_POLICY.md`, LLVM AIToolPolicy).
- Automated scanner false-positive `hard_ban` on `rust-lang/rust` / `PyO3/pyo3` corrected after reading live policy (disclosure/constrained, not absolute ban).
- No tracker comments, forks, or third-party PRs from this survey pass.
- scored_at: `2026-09-08T08:05:00Z`
