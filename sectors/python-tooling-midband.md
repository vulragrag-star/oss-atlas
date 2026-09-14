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

## Product deepen midband subset (2026-09-10, +27 scored)

Account: `vulragrag-star` · Curated product DB/storage homes still missing after prior python-tooling passes · Policy via `raw.githubusercontent.com` · **19** proceed / **8** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 24, 'disclosure': 1, 'hard_ban': 1, 'hostility_risk': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `python-jsonschema/jsonschema` | 4977 | silent | JSON Schema validator; schema/path/ref edges | schema/$ref/path edge + py tests |
| `sqlalchemy/alembic` | 4385 | silent | DB migration tool; path/revision/script edges | revision/path/script edge + py tests |
| `pallets-eco/flask-sqlalchemy` | 4307 | silent | Flask↔SQLAlchemy glue; config/path/model edges | config/session/path edge + py tests |
| `inducer/pudb` | 3248 | silent | Full-screen console debugger; path/config edges | breakpoint/path/config edge + py tests |
| `pallets/itsdangerous` | 3132 | silent | Signer utility; payload/salt edges | signer/payload/salt edge + py tests |
| `intoli/exodus` | 3011 | silent | Relocate ELF bins + deps; path/ELF edges | ELF/path/library edge + py tests |
| `aws-cloudformation/cfn-lint` | 2638 | silent | CloudFormation linter CLI; template/path/rule edges | template/path/rule edge + py tests |
| `agronholm/anyio` | 2538 | silent | Async compatibility layer; backend/path edges | backend/path/cancel edge + py tests |
| `dosisod/refurb` | 2532 | silent | Python refactoring linter; AST/path edges | AST/check/path edge + py fixtures |
| `simonw/sqlite-utils` | 2167 | silent | SQLite CLI+Python; SQL/path/schema edges | SQL/path/schema edge + py tests |
| `pallets-eco/blinker` | 2092 | silent | Signal/event dispatch; sender/receiver edges | signal/sender edge + py tests |
| `pypiserver/pypiserver` | 2067 | silent | Minimal PyPI server; path/upload/index edges | upload/path/index edge + py tests |
| `pytest-dev/pluggy` | 1690 | silent | Pytest plugin system; hook/path edges | hookimpl/path edge + py tests |
| `pallets-eco/wtforms` | 1580 | silent | Form validation; field/parse edges | field/validate/parse edge + py tests |
| `jaraco/keyring` | 1512 | silent | Credential store CLI/lib; backend/path edges | backend/path/service edge + py tests |
| `pytest-dev/pytest-bdd` | 1462 | silent | BDD plugin for pytest; feature/path edges | feature/path/step edge + py tests |
| `pydantic/pydantic-settings` | 1454 | silent | Settings management; env/path/dotenv edges | env/path/dotenv edge + py tests |
| `hynek/stamina` | 1446 | disclosure | Retry library; config/backoff edges — AI disclosure like attrs | retry/backoff/config edge + py tests — disclose AI |
| `marshmallow-code/webargs` | 1407 | silent | HTTP arg parsing; schema/location edges | schema/location/parse edge + py tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `joblib/joblib` | 4390 | silent | Parallel/ML helper lib — weak CLI/parser/packaging hunk class |
| `jmcnamara/XlsxWriter` | 3972 | silent | Spreadsheet writer lib — leave document-format libs |
| `django/daphne` | 2685 | hostility_risk | Django ASGI server — same Django hostility_risk circle as channels |
| `Ericsson/codechecker` | 2615 | silent | Primarily C/C++/Java analyzer stack — not python-tooling product home |
| `python-security/pyt` | 2200 | silent | Legacy Python taint analyzer; quiet/obsolete surface — skip |
| `mahmoud/glom` | 2164 | hard_ban | PR template NO-AI / rejects AI-assisted contributions |
| `nschloe/perfplot` | 1386 | silent | Microbench plotting helper — weak contribution farm |
| `facelessuser/pymdown-extensions` | 1130 | silent | Markdown extension pack — docs-adjacent; weak path/quoting farm |

Notes: Prefer pytest/plugin/packaging/settings edges (pluggy, pytest-bdd, pydantic-settings, keyring, webargs, refurb, sqlite-utils, cfn-lint, pudb). Leave codechecker (non-Python core), legacy pyt, perfplot, and docs-theme extensions.

## Product deepen-2 midband subset (2026-09-11, +66 scored)

Account: `vulragrag-star` · Curated python packaging/CLI/HTTP/async/test/docs-engine product homes still missing after prior product deepen · Policy via `raw.githubusercontent.com` · **54** proceed / **12** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 60, 'disclosure': 5, 'agentscan': 1}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `ets-labs/python-dependency-injector` | 4911 | silent | DI framework; provider/path edges | provider/path edge + tests |
| `strawberry-graphql/strawberry` | 4713 | disclosure | Disclosure GraphQL lib; schema/path edges | schema/path edge + tests — AI policy |
| `spec-first/connexion` | 4611 | silent | OpenAPI-first framework; spec path/validation edges | OpenAPI path / validation edge + tests |
| `miguelgrinberg/python-socketio` | 4368 | disclosure | Disclosure Socket.IO; path/namespace edges | namespace/path edge + tests — disclose AI |
| `MongoEngine/mongoengine` | 4350 | silent | Mongo ODM; field/path/query edges | field/path / query edge + tests |
| `Pylons/pyramid` | 4098 | silent | Web framework; path/config/tween edges | config path / tween edge + tests |
| `encode/databases` | 3993 | silent | Async DB toolkit; URL/path/dialect edges | DB URL / dialect path edge + tests |
| `wjakob/nanobind` | 3705 | silent | C++/Python bindings; stub/path edges | stub/path edge + tests |
| `sloria/doitlive` | 3580 | silent | Live demo shell recorder; path/script edges | script path / prompt edge + tests |
| `jarun/ddgr` | 3542 | silent | DuckDuckGo CLI; argv/quoting edges | argv/query quoting edge + tests |
| `decalage2/oletools` | 3414 | silent | OLE/Office parse CLIs; path/stream edges | OLE path / stream parse edge + tests |
| `pyeve/cerberus` | 3283 | silent | Validation schema lib; schema/path edges | schema/path edge + tests |
| `Tinche/aiofiles` | 3259 | silent | Async file IO; path open edges | path open / mode edge + tests |
| `dalibo/pg_activity` | 3036 | silent | Postgres activity top CLI; conn/path edges | conn info / query path edge + tests |
| `python-arq/arq` | 3012 | silent | Async Redis job queue; job/path/serialize edges | job serialize / Redis path edge + tests |
| `kevin1024/vcrpy` | 3008 | silent | HTTP cassette mock; cassette path/filter edges | cassette path / filter edge + tests |
| `kislyuk/yq` | 2975 | silent | YAML/XML/TOML jq wrapper CLI; path/quoting edges | path/quoting / filter edge + tests |
| `yaml/pyyaml` | 2941 | silent | YAML parser; path/loader edges | loader/path edge + tests |
| `smithyhq/sqladmin` | 2822 | silent | SQLAlchemy admin for FastAPI; model/path edges | model path / admin mount edge + tests |
| `python-gino/gino` | 2790 | silent | Async SQLAlchemy dialect; query/path edges | query/path edge + tests |
| `mozilla/bleach` | 2766 | silent | HTML sanitizer; filter/path edges | filter/protocol path edge + tests |
| `BeanieODM/beanie` | 2698 | silent | Async Mongo ODM; model/path/query edges | query/path / model edge + tests |
| `litl/backoff` | 2695 | silent | Retry decorators; predicate edges | predicate / jitter edge + tests |
| `rthalley/dnspython` | 2674 | silent | DNS toolkit; name/path parse edges | name/parse edge + tests |
| `bczsalba/pytermgui` | 2673 | silent | TUI framework; markup/path edges | markup/path edge + tests |
| `nolar/kopf` | 2635 | silent | K8s operator framework; handler/path edges | handler/path / CRD edge + tests |
| `dateutil/dateutil` | 2633 | silent | Date utilities; parse/tz edges | parse/tz edge + tests |
| `hbldh/bleak` | 2515 | silent | Async BLE client; device/path edges | device path / GATT edge + tests |
| `RDFLib/rdflib` | 2510 | silent | RDF toolkit; graph/path/format edges | graph path / format edge + tests |
| `fastapi/asyncer` | 2490 | silent | Async DX helpers; sync/async bridge edges | bridge/path edge + tests |
| `pytest-dev/pytest-testinfra` | 2477 | silent | Infra tests via pytest; host/path edges | host/path edge + tests |
| `SCons/scons` | 2418 | disclosure | Disclosure build tool; SConstruct path/parser edges | SConstruct path / scanner edge + tests — disclose AI |
| `Neoteroi/BlackSheep` | 2359 | silent | ASGI web framework; route/path/headers edges | route/path/header edge + tests |
| `taskiq-python/taskiq` | 2330 | silent | Async task queue; broker/path edges | broker path / task name edge + tests |
| `testcontainers/testcontainers-python` | 2293 | silent | Docker testcontainers; image/mount path edges | image/mount path edge + tests |
| `pygments/pygments` | 2206 | silent | Syntax highlighter; lexer/path edges | lexer/path edge + tests |
| `gabrielfalcao/HTTPretty` | 2156 | silent | HTTP socket mock; URL/path edges | URL/path match edge + tests |
| `miguelgrinberg/microdot` | 2145 | disclosure | Disclosure tiny web framework; route/path edges | route/path edge + tests — disclose AI |
| `Kludex/mangum` | 2136 | silent | ASGI↔Lambda adapter; event/path edges | event path / handler edge + tests |
| `blade-build/blade-build` | 2105 | silent | Build system; BUILD path/parser edges | BUILD path / target edge + tests |
| `pydoit/doit` | 2083 | silent | CLI task automation; task/path edges | task path / dependency edge + tests |
| `nat-n/poethepoet` | 2073 | silent | Task runner for poetry/uv; task/path edges | task path / env quoting edge + tests |
| `pybuilder/pybuilder` | 2042 | silent | Python build automation; path/plugin edges | plugin/path edge + tests |
| `rubik/radon` | 2019 | silent | Code metrics CLI; path/JSON edges | path / JSON report edge + tests |
| `cherrypy/cherrypy` | 1946 | silent | OO HTTP framework; config/path/tool edges | config path / tool hook edge + tests |
| `python-greenlet/greenlet` | 1845 | silent | Green threads runtime; switch/stack edges with C tests | switch/stack edge + C tests |
| `pydantic/pydantic-core` | 1766 | silent | Pydantic Rust core; validator/path edges | validator/path edge + tests |
| `simplejson/simplejson` | 1710 | silent | JSON lib; encode/path edges | encode/path edge + tests |
| `pgjones/hypercorn` | 1610 | silent | ASGI server; config/path/HTTP2 edges | config path / bind arg edge + tests |
| `Pylons/waitress` | 1598 | silent | Pure-Python WSGI server; path/header parse edges | path / header parse edge + tests |
| `astral-sh/ruff-lsp` | 1505 | silent | Ruff LSP bridge; path/config edges — careful astral sibling policy | path/config edge + tests — human-owned |
| `eventlet/eventlet` | 1275 | silent | Concurrent networking lib; hub/patch path edges | hub/path / monkey-patch edge + tests |
| `PyCQA/pydocstyle` | 1116 | silent | Docstring linter; path/convention edges | path/convention parse edge + tests |
| `python-hyper/h2` | 1041 | silent | HTTP/2 protocol lib; frame/path edges | frame/path edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `carltongibson/django-filter` | 4684 | silent | Django ecosystem — FastAPI/Django hostility_risk farm |
| `Kinto/kinto` | 4417 | silent | JSON sync service app — weak playbook hunk class |
| `elastic/elasticsearch-py` | 4386 | silent | ES client-only — leave |
| `prometheus/client_python` | 4369 | silent | Metrics client lib — weak path/quoting farm |
| `bchao1/bullet` | 3612 | silent | Prompt UI toy — weak product surface |
| `pradyunsg/furo` | 3583 | silent | Sphinx theme skin — prefer sphinx product-code homes |
| `open-telemetry/opentelemetry-python` | 2629 | disclosure | OTel SDK umbrella — prefer smaller product CLIs |
| `qwj/python-proxy` | 2205 | silent | Proxy/tunnel tool — networking-distributed sector |
| `getsentry/sentry-python` | 2202 | silent | Vendor SDK client — leave |
| `RobertCraigie/prisma-client-py` | 2095 | silent | Generated client-only ORM wrapper — leave |
| `kivy/buildozer` | 2030 | silent | Mobile packager — leave mobile packaging |
| `aio-libs/aiomysql` | 1895 | agentscan | AgentScan adopter/org blacklist |

Notes: Prefer midband CLI/parser/test satellites (radon/doit/poethepoet/yq/json_repair/ddgr/ngxtop/s-tui/pg_activity). Leave client-only SDKs and mobile packagers.

## Midband product deepen (2026-09-12, +58 scored)

Account: `vulragrag-star` · Curated python-tooling midband (1k–5k★) packaging/config/HTTP/async/ORM/test/CLI/docs leftovers still missing after prior python product deepens · Policy via `raw.githubusercontent.com` · **44** proceed / **14** leave · No fork/PR/comment.

Policy histogram (this pass): `{'disclosure': 4, 'silent': 50, 'agentscan': 4}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `mongodb/mongo-python-driver` | 4358 | disclosure | Official PyMongo driver; BSON/URI/codec edges with tests — disclose AI assist | URI/BSON/codec edge + tests — disclose AI assist |
| `dynaconf/dynaconf` | 4326 | silent | Python config management CLI/lib; env/file merge edges with tests | config merge/env path edge + tests |
| `more-itertools/more-itertools` | 4089 | silent | stdlib-adjacent iterable utilities; recipe/edge-case unit tests | iterable recipe edge + tests |
| `rspeer/python-ftfy` | 4064 | silent | Unicode mojibake repair library; encoding edge cases with tests | encoding/mojibake edge + tests |
| `pallets/quart` | 3668 | silent | Async Flask-like microframework; ASGI/routing/path edges with tests | ASGI routing/path edge + tests |
| `aws-powertools/powertools-lambda-python` | 3285 | silent | AWS Lambda Powertools; logger/tracer/parser helpers with tests | parser/logger/env edge + tests |
| `lxml/lxml` | 3055 | silent | XML/HTML toolkit; parse/xpath/serialize edges with tests | xpath/parse/serialize edge + tests |
| `scrapinghub/dateparser` | 2855 | silent | Human-date parser; locale/format edge cases with tests | date locale/format parse edge + tests |
| `Textualize/trogon` | 2844 | silent | Click→TUI auto UI; option/path rendering edges with tests | Click option/path TUI edge + tests |
| `psycopg/psycopg` | 2490 | silent | Modern PostgreSQL adapter; connection/type/copy edges with tests | conninfo/type/copy edge + tests |
| `omry/omegaconf` | 2431 | silent | Hierarchical config system; merge/interpolate edges with tests | config merge/interpolate edge + tests |
| `ariebovenberg/whenever` | 2402 | silent | Type-safe datetime/DST library; timezone edge cases with tests | DST/timezone parse edge + tests |
| `piccolo-orm/piccolo` | 1939 | silent | Friendly async/sync ORM + migrations; query/schema edges with tests | query/migration schema edge + tests |
| `Knio/dominate` | 1827 | silent | Python HTML document builder; tag/attribute escape edges with tests | HTML tag/attr escape edge + tests |
| `ormar-orm/ormar` | 1802 | silent | Async pydantic ORM; relation/validation edges with tests | ORM relation/validation edge + tests |
| `crdoconnor/strictyaml` | 1626 | silent | Type-safe YAML subset parser; validation edges with tests | YAML validate/parse edge + tests |
| `hauntsaninja/pyp` | 1531 | silent | Shell-friendly Python runner; argv/pipe edge cases with tests | argv/stdin pipe edge + tests |
| `pallets-eco/flask-wtf` | 1510 | silent | Flask-WTF forms/CSRF; form/csrf edge cases with tests | CSRF/form validation edge + tests |
| `requests-cache/requests-cache` | 1501 | disclosure | Persistent HTTP cache for requests; key/expiry edges — disclose AI assist | cache key/expiry edge + tests — disclose AI assist |
| `mosquito/aio-pika` | 1475 | silent | Async AMQP client; channel/queue declare edges with tests | AMQP queue/channel edge + tests |
| `closeio/tasktiger` | 1467 | silent | Redis task queue; retry/schedule edges with tests | task retry/schedule edge + tests |
| `ionelmc/pytest-benchmark` | 1450 | silent | pytest benchmark fixture; timing/compare edges with tests | benchmark compare/fixture edge + tests |
| `dbcli/mssql-cli` | 1416 | silent | SQL Server CLI with completion; query/format edges with tests | SQL CLI format/completion edge + tests |
| `executablebooks/markdown-it-py` | 1360 | silent | CommonMark-compliant Markdown parser; plugin/token edges with tests | markdown token/plugin edge + tests |
| `redis/redis-om-python` | 1316 | silent | Redis object mapping; model/index edges with tests | OM model/index edge + tests |
| `ParallelSSH/parallel-ssh` | 1282 | silent | Async parallel SSH client; host/cmd edge cases with tests | SSH host/cmd edge + tests |
| `BrianPugh/cyclopts` | 1251 | silent | Type-hint CLI framework; parse/coerce edges with tests | CLI type coerce/parse edge + tests |
| `chinapandaman/PyPDFForm` | 1249 | silent | PDF form fill library/CLI; field/path edges with tests | PDF form field/path edge + tests |
| `devpi/devpi` | 1222 | silent | PyPI staging/test server; upload/index edges with tests | index/upload/path edge + tests |
| `tmux-python/libtmux` | 1206 | silent | Python tmux API wrapper; session/pane edges with tests | tmux session/pane edge + tests |
| `nbQA-dev/nbQA` | 1205 | silent | Run ruff/mypy/etc on notebooks; path/cell edges with tests | notebook path/cell lint edge + tests |
| `itamarst/eliot` | 1188 | silent | Causal logging library; action/serialize edges with tests | log action/serialize edge + tests |
| `art049/odmantic` | 1175 | silent | MongoDB ODM for asyncio; model/query edges with tests | ODM model/query edge + tests |
| `seddonym/import-linter` | 1174 | silent | Architecture import linter; contract/path edges with tests | import contract/path edge + tests |
| `taverntesting/tavern` | 1160 | silent | pytest plugin for HTTP APIs; YAML spec edges with tests | HTTP YAML spec/assert edge + tests |
| `prkumar/uplink` | 1139 | silent | Declarative HTTP client; consumer/path edges with tests | HTTP consumer/path edge + tests |
| `brentyi/tyro` | 1108 | silent | CLI from type hints/config objects; parse edges with tests | CLI type/config parse edge + tests |
| `linkchecker/linkchecker` | 1076 | silent | Link checker CLI; URL/crawl edges with tests | URL crawl/check edge + tests |
| `cheshirekow/cmake_format` | 1072 | silent | CMake listfile formatter; parse/format edges with tests | cmake parse/format edge + tests |
| `python-attrs/cattrs` | 1051 | disclosure | attrs/dataclass converters; structure/unstructure edges — disclose AI assist | structure/unstructure edge + tests — disclose AI assist |
| `requests/toolbelt` | 1039 | silent | requests utilities (multipart/auth); helper edge cases with tests | multipart/auth helper edge + tests |
| `tarpas/pytest-testmon` | 1014 | silent | Select tests affected by changes; depgraph edges with tests | test selection/depgraph edge + tests |
| `desgeeko/pdfsyntax` | 1010 | silent | PDF inspect/modify library; object/stream edges with tests | PDF object/stream edge + tests |
| `samuelcolvin/dirty-equals` | 1004 | silent | Flexible equality helpers for tests; matcher edges with tests | test matcher/equals edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `pydata/xarray` | 4193 | disclosure | Scientific N-D arrays mega-adjacent — leave data-science spill |
| `python-excel/xlrd` | 2206 | silent | Legacy Excel reader; maintainers steer to openpyxl — leave |
| `faust-streaming/faust` | 1887 | silent | Kafka stream processing fork — leave networking/streaming spill |
| `pyca/bcrypt` | 1503 | silent | Crypto primitive — leave for security-crypto sector |
| `FreeOpcUa/opcua-asyncio` | 1478 | silent | Industrial OPC UA stack — niche IoT leave |
| `secretlint/secretlint` | 1448 | silent | TypeScript secrets linter — wrong sector (security/editors spill) |
| `aio-libs/aiocache` | 1437 | agentscan | AgentScan adopter/org blacklist — leave aio-libs circle |
| `aio-libs/aiopg` | 1431 | agentscan | AgentScan adopter/org blacklist — leave aio-libs circle |
| `aio-libs/aiobotocore` | 1425 | agentscan | AgentScan adopter/org blacklist — leave aio-libs circle |
| `aio-libs/aiokafka` | 1403 | agentscan | AgentScan adopter/org blacklist — leave aio-libs circle |
| `domainaware/parsedmarc` | 1294 | silent | DMARC email security parser — leave security spill |
| `uiri/toml` | 1135 | silent | Legacy TOML lib; prefer tomli/tomllib — leave stale |
| `jaraco/inflect` | 1084 | silent | English inflection helpers — thin library leave |
| `spyoungtech/ahk` | 1032 | silent | AutoHotkey GUI automation wrapper — weak product-code farm |

Notes: Prefer midband python product homes (config/packaging leftovers, ASGI/HTTP clients, ORM/queue adapters, pytest plugins, type-hint CLIs, Markdown/PDF/XML parsers, Redis/Mongo OMs). Disclosure: mongo-python-driver/requests-cache/cattrs. Leave AgentScan aio-libs circle (aiocache/aiopg/aiobotocore/aiokafka), science spill (xarray), streaming/IoT/security spills (faust/opcua/parsedmarc/secretlint), crypto primitive (bcrypt), legacy toml/xlrd, thin inflect, AHK GUI wrapper.

## Midband product deepen-2 (2026-09-13, +123 scored)

Account: `vulragrag-star` · Curated python-tooling midband (1k–5k★) leftover product packaging/lint/test/type/AST/HTTP/CLI homes after prior python-tooling midband product deepen · Policy via `raw.githubusercontent.com` · **54** proceed / **69** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 118, 'disclosure': 5}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `jazzband/django-silk` | 4993 | silent | Django profiling/inspection middleware; request path timing edges with tests | profile/path timing edge + tests |
| `grantjenks/python-sortedcontainers` | 3982 | silent | Sorted list/dict/set containers; insertion/bisect edges with tests | bisect/insert order edge + tests |
| `tartley/colorama` | 3796 | silent | Cross-platform colored terminal text; ANSI/Win32 edge cases with tests | ANSI/Win32 color escape edge + tests |
| `flasgger/flasgger` | 3744 | silent | Flask OpenAPI/Swagger UI helper; schema/path edges with tests | OpenAPI schema/path edge + tests |
| `kennethreitz/responder` | 3617 | silent | Familiar HTTP service framework; route/path edges with tests | HTTP route/path edge + tests |
| `axnsan12/drf-yasg` | 3545 | silent | DRF Swagger/OpenAPI 2 schema generator; path/schema edges with tests | Swagger schema/path edge + tests |
| `tomerfiliba/plumbum` | 3051 | silent | Shell combinators CLI/lib; path/quoting/pipe edges with tests | path/quoting/pipe CLI edge + tests |
| `tfranzel/drf-spectacular` | 2860 | silent | DRF OpenAPI 3 schema generator; serializer/path edges with tests | OpenAPI serializer/path edge + tests |
| `chardet/chardet` | 2667 | silent | Character encoding detector; charset/BOM edge cases with tests | charset/BOM detect edge + tests |
| `uqfoundation/dill` | 2449 | silent | Extended Python serializer; pickle protocol/path edges with tests | serialize/protocol path edge + tests |
| `miguelgrinberg/Flask-Migrate` | 2404 | disclosure | Flask-Alembic migrations CLI; migrate/path edges — disclose AI assist | migration path/CLI edge + tests — disclose AI assist |
| `fastapiutils/fastapi-utils` | 2309 | silent | Reusable FastAPI utilities; dependency/timing edges with tests | dependency/timing helper edge + tests |
| `msgpack/msgpack-python` | 2104 | silent | MessagePack serializer; pack/unpack type edges with tests | pack/unpack type edge + tests |
| `laurentS/slowapi` | 2057 | silent | Starlette/FastAPI rate limiter; key/path edges with tests | rate-limit key/path edge + tests |
| `openapi-generators/openapi-python-client` | 1988 | silent | OpenAPI→modern Python client codegen; schema/path edges with tests | OpenAPI client codegen path edge + tests |
| `omnilib/aiomultiprocess` | 1925 | silent | Async multiprocess helpers; pool/path edges with tests | async pool/process edge + tests |
| `rholder/retrying` | 1922 | silent | General-purpose retry decorator lib; backoff/exception edges with tests | retry/backoff exception edge + tests |
| `long2ice/fastapi-cache` | 1867 | silent | FastAPI response/function cache; key/ttl edges with tests | cache key/ttl edge + tests |
| `alecthomas/voluptuous` | 1850 | silent | Python data validation library; schema/coerce edges with tests | schema validate/coerce edge + tests |
| `alexmojaki/heartrate` | 1840 | silent | Realtime Python execution visualizer; path/trace edges with tests | trace/path viz edge + tests |
| `requests/requests-oauthlib` | 1774 | silent | OAuthlib support for Requests; token/redirect edges with tests | OAuth token/redirect edge + tests |
| `danielgtaylor/python-betterproto` | 1769 | silent | Protobuf 3 codegen & library; schema/wire edges with tests | protobuf schema/wire edge + tests |
| `ronf/asyncssh` | 1757 | silent | Async SSH client/server; channel/path/auth edges with tests | SSH channel/path/auth edge + tests |
| `django/asgiref` | 1632 | silent | ASGI spec utilities; sync/async bridge edges with tests | ASGI sync/async bridge edge + tests |
| `spotify/dh-virtualenv` | 1628 | silent | Debian-packaged Python virtualenvs; path/build edges with tests | deb/venv path build edge + tests |
| `cruft/cruft` | 1587 | silent | Cookiecutter template sync/update CLI; path/diff edges with tests | template sync/path diff edge + tests |
| `Teemu/pytest-sugar` | 1533 | silent | pytest progress/UX plugin; report/path edges with tests | pytest report/path plugin edge + tests |
| `litestar-org/polyfactory` | 1505 | silent | Mock data factories for pydantic/msgspec; schema/factory edges with tests | factory/schema generate edge + tests |
| `pdbpp/pdbpp` | 1465 | silent | Drop-in pdb++ debugger; sticky/path command edges with tests | debugger cmd/path sticky edge + tests |
| `wemake-services/django-modern-rest` | 1451 | disclosure | Typed async Django REST framework; schema/path edges — disclose AI assist | REST schema/path edge + tests — disclose AI assist |
| `pydantic/httpx2` | 1430 | silent | Next-gen HTTP client; URL/header/redirect edges with tests | HTTP URL/header/redirect edge + tests |
| `koxudaxi/fastapi-code-generator` | 1406 | silent | OpenAPI→FastAPI codegen CLI; schema/path edges with tests | OpenAPI codegen path/schema edge + tests |
| `sloria/environs` | 1370 | silent | Env var parsing helpers; cast/path edges with tests | env cast/parse edge + tests |
| `datafolklabs/cement` | 1349 | silent | Python application CLI framework; plugin/config path edges with tests | CLI plugin/config path edge + tests |
| `tonybaloney/wily` | 1327 | silent | Python complexity/timing tracker CLI; path/report edges with tests | complexity path/report edge + tests |
| `pschanely/CrossHair` | 1324 | silent | Symbolic analysis / contract testing tool; path/AST edges with tests | contract/AST path edge + tests |
| `marshmallow-code/apispec` | 1219 | silent | Pluggable OpenAPI spec generator; plugin/schema edges with tests | OpenAPI plugin/schema edge + tests |
| `yezz123/authx` | 1196 | silent | FastAPI auth/OAuth2 helpers; token/path edges with tests | auth token/path edge + tests |
| `arskom/spyne` | 1151 | silent | Transport-agnostic RPC framework; serialize/protocol edges with tests | RPC serialize/protocol edge + tests |
| `buildinspace/peru` | 1146 | silent | Generic include-other-people's-code package manager; path/sync edges with tests | fetch/sync path edge + tests |
| `apiflask/apiflask` | 1136 | disclosure | Lightweight web API framework; schema/path edges — disclose AI assist | API schema/path edge + tests — disclose AI assist |
| `CCExtractor/vardbg` | 1113 | silent | Python debugger/profiler with animated viz; path edges with tests | debug/profile path edge + tests |
| `samuelcolvin/python-devtools` | 1077 | silent | Python debug/dev helpers; pretty/path edges with tests | devtools pretty/path edge + tests |
| `patx/pickledb` | 1070 | silent | orjson-backed in-memory key-value store; key/path edges with tests | KV key/serialize edge + tests |
| `jowilf/starlette-admin` | 1031 | silent | Starlette/FastAPI admin UI framework; route/path edges with tests | admin route/path edge + tests |
| `adamchainz/time-machine` | 997 | silent | Test time-travel library; clock/timezone edges with tests | time freeze/tz edge + tests |
| `tox-dev/platformdirs` | 983 | silent | Platform-specific directory helpers; path/OS edges with tests | platform path/OS edge + tests |
| `tox-dev/filelock` | 973 | silent | Platform-independent file lock; lock/path edges with tests | file lock/path edge + tests |
| `borntyping/python-colorlog` | 964 | silent | Colored logging formatter; format/level edges with tests | log format/color edge + tests |
| `pypa/setuptools-scm` | 952 | silent | SCM-tag version management for packaging; tag/path edges with tests | SCM version/tag path edge + tests |
| `PyCQA/autoflake` | 952 | silent | Remove unused imports/vars CLI; AST/path edges with tests | AST unused-import path edge + tests |
| `Fatal1ty/mashumaro` | 937 | silent | Fast serialization library; codec/schema edges with tests | serialize codec/schema edge + tests |
| `pallets-eco/flask-caching` | 934 | silent | Flask caching extension; key/backend edges with tests | cache key/backend edge + tests |
| `twisted/towncrier` | 921 | silent | Release notes manager CLI; fragment/path edges with tests | news fragment/path edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `dpgaspar/Flask-AppBuilder` | 4961 | silent | App builder platform/GUI mega — leave PaaS-adjacent |
| `pydantic/logfire` | 4473 | disclosure | AI observability / LLM platform spill — leave |
| `open-webui/mcpo` | 4371 | silent | MCP/OpenAPI proxy agent-kit adjacent — leave |
| `ktbyers/netmiko` | 4280 | silent | Network device SSH automation — networking spill |
| `agermanidis/autosub` | 4189 | silent | Abandoned subtitle generator — leave abandoned |
| `shobrook/rebound` | 4115 | silent | Stack Overflow CLI novelty — weak product farm |
| `donnemartin/haxor-news` | 4089 | silent | HN browser CLI novelty — leave |
| `chrippa/livestreamer` | 3863 | silent | Unmaintained stream extractor — leave abandoned |
| `insanum/gcalcli` | 3762 | silent | Google Calendar CLI — cloud/service spill |
| `zappa/Zappa` | 3694 | silent | Serverless deploy platform — devops/cloud spill |
| `hypothesis/h` | 3180 | silent | Web annotation product (not HypothesisWorks/hypothesis) — wrong product |
| `OpenStitching/stitching` | 2622 | silent | Image stitching CV — science/vision spill |
| `gaasedelen/lighthouse` | 2580 | silent | RE coverage explorer — security/RE spill |
| `hhursev/recipe-scrapers` | 2225 | silent | Recipe scraping — wrong-sector spill |
| `youyuge34/PI-REC` | 2057 | silent | Image reconstruction DL — ML spill |
| `vibheksoni/stealth-browser-mcp` | 2055 | silent | Anti-bot browser MCP agent kit — leave |
| `astral-sh/ruff-pre-commit` | 2011 | silent | Thin pre-commit hook wrapper for Ruff — thin wrapper |
| `bitly/data_hacks` | 1976 | silent | One-off data CLI hacks — thin/personal |
| `google-deepmind/mathematics_dataset` | 1967 | silent | ML dataset generator — science/ML spill |
| `ravendevteam/talon` | 1950 | silent | Windows tweaker GUI — leave |
| `can4hou6joeng4/boss-agent-cli` | 1950 | silent | Job-site agent CLI — agent kit leave |
| `nix-community/NUR` | 1948 | silent | Nix user repo — devops/nix spill |
| `deadc0de6/dotdrop` | 1947 | silent | Dotfiles deployer — personal/dotfiles leave |
| `everythingishacked/Semaphore` | 1938 | silent | Gesture keyboard novelty — leave |
| `weaviate/elysia` | 1922 | silent | Weaviate platform backend — ML/vector spill |
| `jjjake/internetarchive` | 1904 | silent | Archive.org API client — thin service wrapper |
| `MontrealCorpusTools/Montreal-Forced-Aligner` | 1883 | silent | Speech alignment science — leave |
| `pmh1314520/WebRPA` | 1880 | silent | No-code RPA GUI — leave |
| `uselotus/lotus` | 1837 | silent | Pricing/billing platform — leave PaaS |
| `TotallyNotChase/glitch-this` | 1792 | silent | Image glitch novelty — leave |
| `HFrost0/bilix` | 1785 | silent | Video download CLI — yt-dlp-adjacent leave |
| `bellingcat/telegram-phone-number-checker` | 1782 | silent | OSINT phone checker — security spill |
| `mozilla/fx-private-relay` | 1779 | silent | Firefox Relay product app — leave |
| `tdryer/hangups` | 1745 | silent | Dead Hangouts client — abandoned leave |
| `python-kasa/python-kasa` | 1744 | silent | IoT smart-home API — IoT leave |
| `jasonacox/tinytuya` | 1740 | silent | IoT Tuya devices — IoT leave |
| `jacebrowning/memegen` | 1737 | silent | Meme API novelty — leave |
| `codecov/codecov-action` | 1710 | silent | GH Action wrapper for Codecov — thin CI wrapper |
| `bee-san/Name-That-Hash` | 1669 | silent | Hash identification — security spill |
| `pypa/packaging.python.org` | 1666 | silent | Packaging user guide docs site — docs-only leave |
| `karanhudia/borg-ui` | 1612 | silent | Borg backup GUI — leave GUI |
| `hardbyte/python-can` | 1594 | silent | CAN bus / automotive IoT — IoT leave |
| `benavlabs/fastcrud` | 1586 | silent | Thin FastAPI CRUD generator — weak farm |
| `liuhuanyong/CrimeKgAssitant` | 1585 | silent | Crime NLP assistant — leave |
| `juand-r/entity-recognition-datasets` | 1573 | silent | NER datasets dump — leave |
| `jazzband/django-pipeline` | 1540 | silent | Django asset packaging — thin Django satellite |
| `konlpy/konlpy` | 1492 | silent | Korean NLP package — science/NLP spill |
| `Greenwolf/ntlm_theft` | 1488 | silent | NTLM hash theft tool — security spill |
| `autopkg/autopkg` | 1480 | silent | macOS software packaging automation — devops spill |
| `psypanda/hashID` | 1470 | silent | Hash type identifier — security spill |
| `tiangolo/pydantic-sqlalchemy` | 1407 | silent | Thin SQLAlchemy↔Pydantic converter — thin wrapper |
| `rpm-software-management/dnf` | 1380 | silent | Linux package manager — OS/devops spill |
| `fnmsd/MySQL_Fake_Server` | 1379 | silent | MySQL fake server for file-read attacks — security spill |
| `0xacb/recollapse` | 1375 | silent | Regex fuzz / bypass helper — security spill |
| `Fabric-Development/fabric` | 1371 | silent | Desktop widget framework (not fabric/fabric) — wrong product |
| `AlfredoSequeida/hints` | 1363 | silent | Linux GUI navigation hints — leave GUI |
| `frol/flask-restplus-server-example` | 1334 | silent | Example/server template — leave templates |
| `meridianlabs-ai/inspect_petri` | 1333 | silent | Alignment auditing agent — agent kit leave |
| `osprey-oss/cookiecutter-uv` | 1328 | silent | Cookiecutter template already-covered class — leave templates |
| `mymarilyn/clickhouse-driver` | 1302 | silent | ClickHouse DB driver — databases spill |
| `testdrivenio/django-on-docker` | 1185 | silent | Dockerizing Django tutorial — leave tutorials |
| `DoTheEvo/ANGRYsearch` | 1159 | silent | Linux file search GUI — leave |
| `w-digital-scanner/w9scan` | 1136 | silent | Web vulnerability scanner — security spill |
| `package-url/purl-spec` | 1109 | disclosure | PURL specification docs — specs-only leave |
| `sibears/IDAGolangHelper` | 1093 | silent | IDA Pro Go helpers — RE/security spill |
| `wintests/pytestDemo` | 1071 | silent | API automation demo/tutorial — leave demos |
| `bterwijn/memory_graph` | 1071 | silent | Teaching/debug viz aid — leave teaching tools |
| `vollib/vollib` | 1022 | silent | Options pricing finance lib — science/finance spill |
| `certifi/python-certifi` | 996 | silent | Root CA bundle distribution — thin data package |

Notes: Prefer midband python-tooling product homes (packaging/env CLIs, linters/formatters/typecheckers, test runners/fixtures/mocks, AST/parsers/codegen, HTTP/ASGI microframeworks & clients, config/CLI libs, async helpers, serialization/validation). Disclosure: Flask-Migrate, django-modern-rest, apiflask. Leave platforms/GUIs, agent kits, IoT, security spills, ML/science, thin wrappers, templates/docs-only, wrong-sector CLIs.

## Midband product deepen-3 (2026-09-14, +120 scored)

Account: `vulragrag-star` · Curated python-tooling midband Python (1k–5k★) leftover packaging/lint/test/HTTP-async/CLI/config/serialize/PDF/ORM-helper product homes after python-tooling deepen-2 and other sector deepen-3s · Policy via `raw.githubusercontent.com` · **56** proceed / **64** leave · No fork/PR/comment.

Policy histogram (this pass): `{'silent': 117, 'disclosure': 3}`.

### PROCEED (this pass)

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `jazzband/tablib` | 4757 | silent | Tabular datasets XLS/CSV/JSON/YAML; format/path edges with tests | tabular format/path edge + tests |
| `graphql-python/graphene-django` | 4393 | silent | GraphQL for Django; schema/resolve edges with tests | GraphQL schema/resolve edge + tests |
| `camelot-dev/camelot` | 3820 | silent | PDF table extraction; parse/path edges with tests | PDF table parse/path edge + tests |
| `Suor/funcy` | 3507 | silent | Functional tools for Python; compose/select edges with tests | compose/select functional edge + tests |
| `Miksus/rocketry` | 3363 | silent | Modern Python scheduling library; schedule/path edges with tests | schedule parse/path edge + tests |
| `celery/kombu` | 3142 | silent | Messaging library for Python; serialize/transport edges with tests | message serialize/transport edge + tests |
| `jazzband/django-redis` | 3086 | silent | Django Redis cache backend; key/serialize edges with tests | cache key/serialize edge + tests |
| `reloadware/reloadium` | 2985 | silent | Hot reload and profiling for Python; path/reload edges with tests | reload/path profile edge + tests |
| `keleshev/schema` | 2946 | silent | Pythonic schema validation; coerce/type edges with tests | schema validate/coerce edge + tests |
| `grantjenks/python-diskcache` | 2906 | silent | Disk-backed cache; path/TTL/evict edges with tests | disk cache path/TTL edge + tests |
| `pikepdf/pikepdf` | 2798 | silent | PDF read/write via QPDF; page/path edges with tests | PDF page/path edge + tests |
| `tkem/cachetools` | 2777 | silent | Extensible memoizing collections; TTL/key edges with tests | cache TTL/key edge + tests |
| `evansd/whitenoise` | 2760 | silent | Static file serving for Python web apps; path/MIME edges with tests | static path/MIME edge + tests |
| `noirbizarre/flask-restplus` | 2731 | silent | Flask REST+docs framework; swagger/path edges with tests | REST swagger/path edge + tests |
| `aboutcode-org/scancode-toolkit` | 2622 | silent | License/copyright/dependency scanner CLI; path/parse edges with tests | scan path/license parse edge + tests |
| `schematics/schematics` | 2586 | silent | Python data structures validation; model/type edges with tests | model/validate type edge + tests |
| `mongodb/motor` | 2525 | silent | Async MongoDB/Tornado driver; query/path edges with tests | async Mongo query/path edge + tests |
| `Tivix/django-rest-auth` | 2416 | silent | Django REST auth helpers; token/path edges with tests | auth token/path edge + tests |
| `xhtml2pdf/xhtml2pdf` | 2391 | silent | HTML-to-PDF via ReportLab; layout/path edges with tests | HTML/PDF layout path edge + tests |
| `agronholm/sqlacodegen` | 2368 | silent | SQLAlchemy model code generator; reflect/path edges with tests | codegen reflect/path edge + tests |
| `mirumee/ariadne` | 2342 | silent | Schema-first GraphQL for Python; schema/path edges with tests | GraphQL schema/path edge + tests |
| `GrahamDumpleton/wrapt` | 2304 | silent | Decorators/wrappers/monkey-patch; wrap/call edges with tests | wrap/decorator call edge + tests |
| `python-restx/flask-restx` | 2234 | silent | Flask-RESTPlus fork; swagger/path edges with tests | REST swagger/path edge + tests |
| `Alir3z4/html2text` | 2170 | silent | HTML to Markdown converter; parse/entity edges with tests | HTML/Markdown parse edge + tests |
| `jeffknupp/sandman2` | 2041 | silent | Auto REST API for legacy DBs; reflect/path edges with tests | REST reflect/path edge + tests |
| `celery/django-celery-beat` | 1953 | silent | Celery periodic tasks via Django ORM; schedule/path edges with tests | beat schedule/path edge + tests |
| `myusuf3/delorean` | 1823 | silent | Datetime helper library; TZ/parse edges with tests | datetime TZ/parse edge + tests |
| `cirospaciari/socketify.py` | 1713 | silent | High-perf HTTP/WS for PyPy/CPython; path/protocol edges with tests | HTTP/WS path/protocol edge + tests |
| `awtkns/fastapi-crudrouter` | 1695 | silent | Dynamic FastAPI CRUD router; path/model edges with tests | CRUD path/model edge + tests |
| `dropbox/PyHive` | 1693 | silent | Python Hive/Presto interface; SQL/path edges with tests | Hive/Presto SQL/path edge + tests |
| `crossbario/autobahn-testsuite` | 1692 | disclosure | WebSocket protocol testsuite; frame/path edges — disclose AI assist | WS frame/path edge + tests — disclose AI assist |
| `pyeventsourcing/eventsourcing` | 1685 | silent | Event sourcing library; store/serialize edges with tests | event store/serialize edge + tests |
| `uriyyo/fastapi-pagination` | 1679 | silent | FastAPI pagination helpers; page/limit edges with tests | pagination page/limit edge + tests |
| `prettytable/prettytable` | 1669 | silent | ASCII table display; align/width edges with tests | table align/width edge + tests |
| `vimalloc/flask-jwt-extended` | 1580 | silent | Flask JWT extension; claim/path edges with tests | JWT claim/path edge + tests |
| `trallnag/prometheus-fastapi-instrumentator` | 1486 | silent | Prometheus metrics for FastAPI; path/metric edges with tests | metrics path/label edge + tests |
| `flask-api/flask-api` | 1473 | silent | Browsable web APIs for Flask; render/path edges with tests | API browse/render path edge + tests |
| `eralchemy/eralchemy` | 1433 | silent | ER diagram generator for SQLAlchemy; parse/path edges with tests | ER diagram parse/path edge + tests |
| `kvesteri/sqlalchemy-utils` | 1345 | silent | SQLAlchemy utils/datatypes; type/path edges with tests | SQLAlchemy type/path edge + tests |
| `miguelgrinberg/Flask-HTTPAuth` | 1289 | disclosure | Flask Basic/Digest/Token auth; auth path edges — disclose AI assist | auth path/header edge + tests — disclose AI assist |
| `emmett-framework/emmett` | 1235 | silent | Python web framework; route/path edges with tests | route/path framework edge + tests |
| `mar10/wsgidav` | 1232 | silent | WebDAV server on WSGI; path/auth edges with tests | WebDAV path/auth edge + tests |
| `alisaifee/flask-limiter` | 1206 | silent | Flask rate limiting; key/path edges with tests | rate-limit key/path edge + tests |
| `pypa/gh-action-pypi-publish` | 1183 | silent | Blessed GitHub Action for PyPI publish; path/token edges with tests | publish path/token edge + tests |
| `jazzband/django-configurations` | 1135 | silent | Django settings by environment; config/env edges with tests | settings env/config edge + tests |
| `python-validators/validators` | 1124 | silent | Human-friendly validators; email/url/path edges with tests | validate email/url/path edge + tests |
| `duo-labs/parliament` | 1123 | silent | AWS IAM linting library; policy/parse edges with tests | IAM policy lint/parse edge + tests |
| `AcademySoftwareFoundation/rez` | 1092 | silent | Package config/build/deploy system; resolve/path edges with tests | package resolve/path edge + tests |
| `tortoise/aerich` | 1082 | silent | TortoiseORM migrations CLI; migrate/path edges with tests | migration path/CLI edge + tests |
| `TypeError/secure` | 1055 | silent | HTTP security headers helper; header/default edges with tests | security header/default edge + tests |
| `sibson/redbeat` | 1051 | silent | Celery Beat Redis scheduler; schedule/key edges with tests | beat schedule/key edge + tests |
| `sebleier/django-redis-cache` | 1040 | silent | Redis cache backend for Django; key/TTL edges with tests | cache key/TTL edge + tests |
| `jfilter/clean-text` | 1028 | silent | Text cleaning utilities; unicode/normalize edges with tests | text clean/normalize edge + tests |
| `daijro/hrequests` | 1022 | silent | Human-friendly HTTP client; header/session edges with tests | HTTP session/header edge + tests |
| `sabuhish/fastapi-mail` | 1011 | silent | FastAPI mail sending; attach/path edges with tests | mail attach/path edge + tests |
| `mongomock/mongomock` | 1003 | silent | Mock pymongo collections; query/filter edges with tests | mock query/filter edge + tests |

### LEAVE (this pass)

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `JakeWharton/pidcat` | 4955 | silent | Android logcat colorizer — mobile/Android spill |
| `cloudtools/troposphere` | 4944 | silent | AWS CloudFormation DSL — cloud/IaC spill |
| `miguelgrinberg/microblog` | 4776 | silent | Flask Mega-Tutorial sample app — tutorial leave |
| `OTRF/ThreatHunter-Playbook` | 4659 | silent | Threat hunting detections — security spill |
| `IDSIA/sacred` | 4378 | silent | ML experiment config/repro — ML science spill |
| `jonaslejon/malicious-pdf` | 4309 | silent | Malicious PDF generator — security/offensive spill |
| `praw-dev/praw` | 4252 | silent | Reddit API wrapper — service/API spill |
| `eclipse-sumo/sumo` | 4177 | silent | Traffic simulation — science/domain spill |
| `opengeos/segment-geospatial` | 4145 | silent | Geospatial ML segmentation — ML/science spill |
| `snipsco/snips-nlu` | 3973 | silent | NLU/NLP package — ML spill |
| `arvin341az-glitch/RVG` | 3972 | silent | Proxy management panel — circumvention/proxy GUI leave |
| `fastapi-admin/fastapi-admin` | 3823 | silent | Admin dashboard GUI mega — leave PaaS-adjacent |
| `geex-arts/django-jet` | 3622 | silent | Django admin theme/GUI — leave |
| `pathwaycom/bdh` | 3555 | silent | ML architecture research — ML spill |
| `zzzeek/sqlalchemy` | 3453 | silent | Unofficial mirror — not product home (official sqlalchemy/sqlalchemy) |
| `Mirix-AI/MIRIX` | 3441 | silent | Multi-agent personal assistant — agent kit leave |
| `batrachianai/toad` | 3429 | disclosure | AI terminal interface — AI/agent leave |
| `pinry/pinry` | 3422 | silent | Image board web app — product GUI leave |
| `resemble-ai/Resemblyzer` | 3303 | silent | Voice DL compare — ML spill |
| `christabor/flask_jsondash` | 3281 | silent | Dashboard builder GUI — leave |
| `milesmcc/shynet` | 3154 | silent | Web analytics product — product/platform leave |
| `tensorflow/agents` | 3026 | silent | TF-Agents RL library — ML spill |
| `tiangolo/uwsgi-nginx-flask-docker` | 3003 | silent | Docker image recipe — devops/image leave |
| `tiangolo/uvicorn-gunicorn-fastapi-docker` | 2915 | silent | Docker image recipe — devops/image leave |
| `aaronsw/html2text` | 2813 | silent | Unmaintained HTML2Markdown — prefer Alir3z4 fork; leave abandoned |
| `flaskbb/flaskbb` | 2660 | silent | Forum software product — app leave |
| `supabase/supabase-py` | 2578 | silent | Supabase BaaS client — platform SDK leave |
| `onekey-sec/unblob` | 2555 | silent | Firmware/container extractor — security/RE spill |
| `fastapi-practices/fastapi-best-architecture` | 2551 | silent | Enterprise FastAPI scaffold — template leave |
| `virtio-win/virtio-win-pkg-scripts` | 2537 | silent | Windows driver packaging scripts — wrong sector |
| `ungoogled-software/ungoogled-chromium-windows` | 2528 | silent | Browser packaging — wrong sector |
| `allegro/ralph` | 2517 | silent | CMDB/asset management product — platform leave |
| `keithrozario/Klayers` | 2506 | silent | AWS Lambda layers packaging — cloud spill |
| `ChrispyBacon-dev/DockFlare` | 2442 | silent | Cloudflare tunnel Docker UI — devops/GUI leave |
| `mjhea0/flaskr-tdd` | 2342 | silent | Flask tutorial/TDD sample — tutorial leave |
| `fairlearn/fairlearn` | 2285 | silent | ML fairness package — ML/science spill |
| `h5py/h5py` | 2252 | silent | HDF5 science I/O — science spill |
| `ramnes/notion-sdk-py` | 2182 | silent | Notion API SDK — service SDK spill |
| `indico/indico` | 2109 | silent | Event management product (CERN) — product leave |
| `greyli/helloflask` | 2079 | silent | Hello Flask tutorial book code — tutorial leave |
| `BetaStreetOmnis/xhs_ai_publisher` | 2076 | silent | AI Xiaohongshu publisher — agent/social leave |
| `SublimeLinter/SublimeLinter` | 2039 | silent | Sublime Text plugin — editors spill |
| `noamgat/lm-format-enforcer` | 2035 | silent | LLM output format enforcer — AI/LLM leave |
| `django-notifications/django-notifications` | 1955 | silent | Notifications app product — app leave |
| `raphaelvallat/pingouin` | 1929 | silent | Stats package — science spill |
| `dynamicslab/pysindy` | 1899 | silent | Dynamical systems ID — science/ML spill |
| `scholarly-python-package/scholarly` | 1880 | silent | Google Scholar scraper — wrong-sector spill |
| `johannfaouzi/pyts` | 1877 | silent | Time series classification — ML spill |
| `Werneror/Poetry` | 1780 | silent | Chinese poetry dataset — wrong product (not packaging) |
| `sindresorhus/editorconfig-sublime` | 1775 | silent | Sublime EditorConfig plugin — editors spill |
| `awslabs/aws-config-rules` | 1738 | silent | AWS Config sample rules — cloud spill |
| `mjun0812/flash-attention-prebuild-wheels` | 1730 | silent | ML wheels prebuild — ML spill |
| `dj-bolt/django-bolt` | 1683 | silent | Django+Rust web framework product — platform leave |
| `Scony/godot-gdscript-toolkit` | 1607 | silent | GDScript tools — game/editors spill |
| `mdhiggins/sickbeard_mp4_automator` | 1586 | silent | Media convertor — media/IoT-adjacent leave |
| `ExpDev07/coronavirus-tracker-api` | 1569 | silent | COVID tracker API — dead/domain leave |
| `amisadmin/fastapi-amis-admin` | 1566 | silent | Admin dashboard GUI — leave |
| `chr0nzz/traefik-manager` | 1562 | silent | Traefik web UI — devops/GUI leave |
| `guillevc/yubal` | 1556 | silent | YouTube Music downloader — media leave |
| `celery/django-celery` | 1551 | silent | Old abandoned Celery-Django project — leave abandoned |
| `HaoZhang95/Python24` | 1547 | silent | Python/ML course notes — tutorial leave |
| `insistence/RuoYi-Vue3-FastAPI` | 1525 | silent | Admin scaffold template — template leave |
| `pysal/pysal` | 1522 | silent | Spatial analysis meta-package — science spill |
| `Parallels/rq-dashboard` | 1522 | silent | RQ queue dashboard GUI — leave |

Notes: Prefer midband Python python-tooling product homes (packaging/build/publish, lint/format/type/AST, test/fixtures/property/mutation, HTTP/async/OpenAPI, CLI frameworks, config/env/serialize/datetime/PDF, ORM/ODM/query helpers that belong in python-tooling). Leave AgentScan (aio-libs), hard AI bans, platforms/GUIs, agent kits, IoT, security spills, ML/science, thin wrappers, templates/docs-only, wrong-sector CLIs (netmiko/zappa/gcalcli/hashID/dnf), disclosure-only leaves as scored.

