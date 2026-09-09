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

## Deepen pass (2026-09-09, +35 scored)

Account: `vulragrag-star` · Curated product midband slice from remaining unscored python-tooling leftovers + curated packaging/lint/test fills · Policy via `raw.githubusercontent.com` · **29** proceed / **6** leave · Band: `1k-5k` · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 33, 'disclosure': 2}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `andreafrancia/trash-cli` | 4579 | silent | XDG trashcan CLI; path/quoting/FS edge cases across platforms | trash path/quoting/FS edge + Python tests |
| `jupyter-book/jupyter-book` | 4277 | silent | Publication-quality Jupyter book builder; path/config/Sphinx edges | docs build/path/config edge + Python tests |
| `Textualize/rich-cli` | 3719 | silent | Rich terminal toolbox CLI; parse/format/path edges | CLI format/path edge + Python tests |
| `DetachHead/basedpyright` | 3583 | silent | Pyright fork with stricter typing; diagnose/config/path edges | typecheck diagnose/config/path edge + tests |
| `commitizen-tools/commitizen` | 3506 | disclosure | Conventional-commit + bump/changelog CLI; config/version provider edges (disclose Generated-by) | commit/bump/config edge + tests; AI disclosure trailer |
| `beartype/beartype` | 3491 | silent | Near-real-time runtime type checker; decorator/typing edges | runtime typecheck/typing edge + Python tests |
| `wemake-services/wemake-python-styleguide` | 2898 | disclosure | Opinionated flake8 styleguide; AST/rule edges (Astral-style AI policy, no autonomous agents) | flake8 AST/rule edge + tests; human-in-loop disclosure |
| `python-lsp/python-lsp-server` | 2593 | silent | Python language server (pylsp); LSP/plugin/path edges | LSP plugin/path/workspace edge + tests |
| `samuelcolvin/watchfiles` | 2534 | silent | Fast file-watch / reload library+CLI; path/FS notify edges | watch path/FS notify edge + Python tests |
| `microsoft/debugpy` | 2469 | silent | Debug Adapter Protocol implementation for Python; path/attach edges | DAP attach/path edge + tests |
| `python-rope/rope` | 2234 | silent | Python refactoring library; AST/rename/move path edges | refactor AST/path edge + Python tests |
| `mkdocstrings/mkdocstrings` | 2092 | silent | MkDocs autodoc from sources; handler/path/config edges | docs handler/path/config edge + tests |
| `prospector-dev/prospector` | 2086 | silent | Meta static-analysis CLI wrapping multiple tools; config/path edges | lint meta config/path edge + tests |
| `pytest-dev/pytest-cov` | 2061 | silent | Coverage plugin for pytest; config/path/report edges | pytest coverage config/path edge + tests |
| `pytest-dev/pytest-mock` | 2038 | silent | pytest wrapper for unittest.mock; fixture API edges | pytest mock fixture edge + tests |
| `GitGuardian/ggshield` | 1995 | silent | Secrets detection/validation CLI; path/scan/config edges | secrets scan path/config edge + tests |
| `jupyter/nbconvert` | 1936 | silent | Jupyter notebook conversion; format/path/template edges | nbconvert format/path/template edge + tests |
| `cpplint/cpplint` | 1849 | silent | Google C++ style linter (Python); path/filter/line edges | lint path/filter edge + Python tests |
| `nickstenning/honcho` | 1711 | silent | Procfile process manager (Foreman clone); env/path edges | Procfile env/path edge + Python tests |
| `pytest-dev/pytest-asyncio` | 1662 | silent | Asyncio support plugin for pytest; mode/fixture edges | pytest asyncio mode/fixture edge + tests |
| `nschloe/tuna` | 1597 | silent | Python profile viewer; profile parse/path edges | profile parse/path edge + Python tests |
| `pytest-dev/pytest-django` | 1546 | silent | Django plugin for pytest; settings/DB fixture edges | pytest django settings/fixture edge + tests |
| `osprey-oss/deptry` | 1475 | silent | Find unused/missing/transitive deps in Python projects; pyproject/path edges | deps pyproject/path edge + tests |
| `PyCQA/pyflakes` | 1459 | silent | Lightweight Python source checker; parse/name edges | pyflakes parse/name edge + tests |
| `boxed/mutmut` | 1430 | silent | Mutation testing system; mutate/path/test edges | mutation path/test edge + Python tests |
| `python-poetry/cleo` | 1353 | silent | Beautiful testable CLI framework (Poetry stack); command/arg edges | CLI command/arg edge + Python tests |
| `adamchainz/django-upgrade` | 1237 | silent | Automatic Django upgrade codemod; AST/version edges | django upgrade AST/version edge + tests |
| `PyCQA/flake8-bugbear` | 1116 | silent | Flake8 plugin for likely bugs/design problems; AST rule edges | flake8 AST rule edge + tests |
| `c4urself/bump2version` | 1115 | silent | Version-bump CLI (bumpversion successor); config/file edges | version bump config/file edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `cookiecutter-flask/cookiecutter-flask` | 4722 | silent | Flask web-app cookiecutter — prefer packaging/tooling templates already mapped |
| `dry-python/returns` | 4360 | silent | Typed FP container library — not packaging/lint/test CLI product surface |
| `CITGuru/PyInquirer` | 1997 | silent | Stale PyInquirer fork (inactive) — prefer prompt_toolkit/questionary homes |
| `gitless-vcs/gitless` | 1949 | silent | Niche Git-overlay VCS; inactive since 2023 — weak python-tooling farm |
| `frappe/bench` | 1725 | silent | Frappe multi-tenant ops CLI — app-framework niche, not general packaging/lint |
| `peritus/bumpversion` | 1519 | silent | Superseded/inactive bumpversion — prefer bump2version/commitizen |

Notes: Prefer packaging/lint/typecheck/pytest-plugin/docs/profile CLI surfaces with regression tests. Leave stale prompt forks, inactive VCS overlays, superseded bumpversion, Flask web cookiecutters, typed FP libraries without a CLI farm, and app-framework ops CLIs (Frappe bench). wemake AI policy is Astral-style disclosure (no autonomous agents); commitizen wants Generated-by disclosure.

