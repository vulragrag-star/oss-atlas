# Sector survey: python-tooling (midband 1k–5k★)

Account: `vulragrag-star` · Input: `survey/raw/python-tooling-midband.jsonl` · Deep-sampled **47** real product repos via `raw.githubusercontent.com` policy files · Hard leaves respected · No fork/PR/comment · Band: `1k-5k`.

Playbook lens: famous main product (1k–5k★), not AgentScan, not hard AI ban, hunk class = **packaging / linter / test-runner / typechecker / AST-tool path-quoting bugs with regression tests** (not ML UIs, not GraphQL apps, not predecessor pypa queues).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 46 | No hard ban found in common CONTRIBUTING/AI paths |
| disclosure | 1 | Explicit AI-assisted / disclosure language |

Proceed: **42** · Leave: **5** · Appended to `survey/scored.jsonl` with `band: "1k-5k"`.

## Hard leaves (playbook — even if outside this band sample)

- Predecessor closed/open pypa queues: `pypa/build`, `pypa/setuptools`, `pypa/distutils`, `pypa/wheel`, `pypa/installer`, `pypa/hatch`, `pypa/cibuildwheel` — never re-enter
- `aio-libs/aiohttp` AgentScan; Cython forever banned
- ML UIs / account-creator noise in raw dump — wrong class

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo’s merged outsider PR voice. Re-run `agentscan-check.py --refresh` + `hostility-scan.py` before any future fork.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `Instagram/MonkeyType` | 4999 | silent | Runtime type annotation collector; stub/path edges | stub/path/runtime-type edge + tests |
| `lk-geimfari/mimesis` | 4838 | silent | Fake-data library for tests; locale/provider edges | provider/locale edge + tests |
| `jendrikseipp/vulture` | 4799 | silent | Dead-code finder; AST/path edges | AST visitor/path edge + tests |
| `pyinvoke/invoke` | 4775 | silent | Pythonic task runner; path/cli/quoting edges | CLI path/quoting/task edge + tests |
| `Qix-/better-exceptions` | 4719 | silent | Pretty exception formatter | traceback format edge + tests |
| `hhatto/autopep8` | 4659 | silent | PEP8 formatter; parse/fix edges | format fix/path edge + tests |
| `Yelp/detect-secrets` | 4633 | silent | Secrets detection CLI; plugin/path edges | plugin/path/baseline edge + tests |
| `scottrogowski/code2flow` | 4606 | silent | Call-graph generator; path/parse edges | parse/path/graph edge + tests |
| `audreyfeldroy/cookiecutter-pypackage` | 4600 | silent | Cookiecutter package template; path/render edges | template path/render edge + tests |
| `pythonprofilers/memory_profiler` | 4574 | silent | Memory profiler; line/path edges | line/path profiler edge + tests |
| `spulec/freezegun` | 4522 | silent | Time-mock for tests; datetime edge cases | datetime freeze edge + tests |
| `unionai-oss/pandera` | 4451 | silent | DataFrame schema validation; schema/path edges | schema/check/path edge + tests |
| `astral-sh/python-build-standalone` | 4392 | silent | Redistributable Python builds; path/platform edges | build/path/platform edge + tests |
| `getsentry/responses` | 4344 | silent | Requests mock utility; URL/match edges | URL match/mock edge + tests |
| `rocky/python-uncompyle6` | 4320 | silent | Bytecode decompiler; version/path edges | bytecode/version/path edge + tests |
| `pex-tool/pex` | 4224 | silent | PEX/lockfile tool; path/env edges | PEX/lock/path/env edge + tests |
| `ansible/molecule` | 4143 | silent | Ansible testing framework; path/scenario edges | scenario/path/driver edge + tests |
| `asottile/pyupgrade` | 4112 | silent | Syntax upgrade + pre-commit hook; AST edges | AST rewrite/path edge + tests |
| `msgspec/msgspec` | 4091 | silent | Fast serialization + validation; schema edges | schema/decode edge + tests |
| `andialbrecht/sqlparse` | 4018 | silent | SQL parser module; tokenize/format edges | SQL tokenize/format edge + tests |
| `datamodel-code-generator/datamodel-code-generator` | 4011 | silent | OpenAPI→Pydantic generator; schema/path edges | schema/path/codegen edge + tests |
| `nvdv/vprof` | 3977 | silent | Visual profiler; path edges | profiler path edge + tests |
| `ansible/ansible-lint` | 3906 | silent | Ansible playbook linter; rule/path edges | lint rule/path edge + tests |
| `FactoryBoy/factory_boy` | 3805 | silent | Test fixtures factory; trait/path edges | factory trait/build edge + tests |
| `coala/coala` | 3595 | silent | Unified lint CLI; bear/path edges — quieter | bear/path/config edge + tests |
| `schemathesis/schemathesis` | 3586 | silent | API property-testing; schema/path edges | schema/path/strategy edge + tests |
| `eliben/pycparser` | 3567 | silent | Pure-Python C99 parser; AST edges | C parse/AST edge + tests |
| `tox-dev/pipdeptree` | 3019 | silent | Dependency tree CLI; path/env edges | dep tree/path/env edge + tests |
| `gotcha/ipdb` | 1975 | silent | IPython pdb; path/embed edges | embed/path edge + tests |
| `typeddjango/django-stubs` | 1973 | disclosure | Django PEP484 stubs; PR template AI policy doc | stub/path/typing edge + tests — follow PR AI checklist |
| `Instagram/LibCST` | 1941 | silent | Concrete syntax tree for Python; parse/transform edges | CST transform/path edge + tests |
| `erikrose/parsimonious` | 1915 | silent | PEG parser; grammar edges | grammar/parse edge + tests |
| `pytest-dev/pytest-xdist` | 1903 | silent | pytest distributed plugin; path/worker edges | worker/path/looponfail edge + tests |
| `patrick-kidger/jaxtyping` | 1864 | silent | Shape/dtype type annotations; check edges | shape/dtype check edge + tests |
| `damnever/pigar` | 1793 | silent | requirements.txt generator; import/path edges | import/path/req edge + tests |
| `r1chardj0n3s/parse` | 1792 | silent | parse() string parser; format-spec edges | format-spec parse edge + tests |
| `ekalinin/nodeenv` | 1791 | silent | Node venv integrator; path/env edges | nodeenv path/env edge + tests |
| `agronholm/typeguard` | 1786 | silent | Runtime type checker; typing edges | typing check/path edge + tests |
| `sumerc/yappi` | 1725 | silent | Multithread profiler; path/clock edges | profiler clock/path edge + tests |
| `tree-sitter/py-tree-sitter` | 1495 | silent | Python bindings to tree-sitter | parse/language/path edge + tests |
| `zubanls/zuban` | 1176 | silent | Python typechecker / language server | typecheck/LSP/path edge + tests |
| `osprey-oss/migrate-to-uv` | 1160 | silent | Poetry/Pipenv→uv migrator; path/lock edges | lock/path/migrate edge + tests |

### Tier notes

**Best first homes (small testable parser/path/format hunks):** start near the top of the proceed table; one home at a time; stay after a merge.

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `ultrajson/ultrajson` | 4496 | silent | JSON C extension library — not packaging/lint/test tooling product |
| `pypi/warehouse` | 4145 | silent | PyPI itself — too large/process-heavy for midband first homes |
| `mitsuhiko/pipsi` | 1993 | silent | Obsolete pip script installer — superseded by pipx |
| `cjolowicz/cookiecutter-hypermodern-python` | 1919 | silent | Template farm — prefer cookiecutter core or packaging tools |
| `python/typing` | 1782 | silent | typing PEPs/docs home — not product tooling code |

## Sector synthesis

- Midband (1k-5k) deep sample: **47** curated product repos.
- Proceed **42** / Leave **5**.
- Disclosure repos: `typeddjango/django-stubs`.
- No AgentScan / fish-style / sqlite-agentic hits inside this midband sample (those hard leaves live in higher-star scored set).
- Method: policy files via `raw.githubusercontent.com` (CONTRIBUTING*/AI*/AGENTS*/PR templates); local AgentScan blacklist only.
- No fork / PR / tracker comment performed.

