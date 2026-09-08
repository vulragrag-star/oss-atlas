# Sector survey: python-tooling

Account: `vulragrag-star` · Input: `survey/raw/python-tooling.jsonl` (65 lines, mostly awesome/AI/app noise) · Deep-sampled **61** real tooling/adjacent repos via GraphQL policy blobs + playbook prior scout · **Excluded predecessor fails** (`pypa/build`, `setuptools`, `distutils`, `wheel`, `installer`, `cibuildwheel`, `hatch`) · No fork/PR/comment.

Playbook lens: famous main product (≥1k★), not AgentScan, not hard AI ban, hunk class = **quoting / parser / path / packaging-backend / env / CLI bugs with regression tests** (not docs farm, not GFI spam, not satellites).

## Policy histogram (scored set)

| Policy class | Count | Notes |
|---|---:|---|
| silent | 38 | Many classic tools still have no AI page |
| disclosure | 14 | pytest/astral/pip/conda/sphinx/copier/cpython/… human-owned AI |
| hostility_risk | 15 | Predecessor fails, Jazzband, pre-commit slop closes, mypy new-contrib LLM discourage, FastAPI/Django |
| hard_ban | 2 | `yt-dlp/yt-dlp` NO AI/LLM; `PyO3/pyo3` no unsolicited AI PRs |
| agentscan | 1 | `aio-libs/aiohttp` |

Proceed: **34** · Leave: **36** · Scored lines appended to `survey/scored.jsonl`.

## PROCEED candidates (contrib fit)

Ranked for playbook hunk class. Prefer one home-repo at a time; copy that repo's merged outsider PR voice. `pytest`/`tox` already known; `ruff`/`uv` **careful AGENTS**.

| Repo | ★ | Policy | Why fit | Sample bug class |
|---|---:|---|---|---|
| `astral-sh/uv` | 89622 | disclosure | CAREFUL: astral AI_POLICY — human-in-loop, no autonomous agents, no AI maintainer comments; high bar | resolver/path/venv edge + Rust tests |
| `pallets/flask` | 73584 | silent | Microframework; path/config/cli edges — prefer click/tox first | cli/path/config edge + tests |
| `scrapy/scrapy` | 64240 | silent | Crawler framework; URL/path/selector edges with tests | URL/path/selector edge + tests |
| `astral-sh/ruff` | 49545 | disclosure | CAREFUL: same astral AI_POLICY; linter/formatter parse edges; not a first-home pick | lint rule/path/parse edge + fixtures |
| `pyenv/pyenv` | 45085 | silent | Shell version manager; PATH/shim/quoting class matches playbook | shim/PATH/quoting edge + bats/shell tests |
| `psf/black` | 41834 | silent | Formatter; AST/parse edge cases with snapshot tests | AST/parse edge + regression fixtures |
| `python-poetry/poetry` | 34295 | silent | Packaging/dependency resolver; lock/path/env edges | lockfile/path/env resolver edge + tests |
| `cookiecutter/cookiecutter` | 25081 | silent | Project template CLI; path/render/hook edges | template path/hook quoting + tests |
| `fastapi/typer` | 19960 | silent | Click-based CLI builder; type/help/arg parse edges | CLI arg/type/help parse edge + tests |
| `pallets/click` | 17656 | silent | Composable CLI toolkit; option/quoting/path parse surface; strong test culture | CLI option/quoting/path parse + tests |
| `microsoft/pyright` | 15625 | silent | Type checker; stub/path/config edges; TypeScript core | stub/path/config edge + tests |
| `Nuitka/Nuitka` | 15122 | disclosure | Compiler; path/import/plugin edges; AGENTS present | import/path/plugin edge + tests |
| `pytest-dev/pytest` | 14489 | disclosure | Welcomes AI with human oversight; bans purely agentic PRs; credit tools — classic assert/path/plugin edges | plugin/path/assertion edge + unit tests |
| `pyinstaller/pyinstaller` | 13088 | silent | Freeze tool; path/hook/analysis edges | analysis/hook/path edge + tests |
| `pypa/pipx` | 12955 | silent | Isolated app installer; venv/path/entry-point edges | venv/path/entry-point edge + tests |
| `HypothesisWorks/hypothesis` | 8946 | disclosure | AI OK if human owns every issue/PR/comment; property-test surface | strategy/example database path edge + tests |
| `pdm-project/pdm` | 8674 | silent | Modern packaging manager; has AGENTS.md for assistants (not a ban); path/lock edges | lock/path/python-finder edge + tests |
| `PyCQA/bandit` | 8251 | silent | Security linter; AST visitor edges with tests | AST visitor/path edge + tests |
| `mamba-org/mamba` | 8089 | silent | Fast package manager; matchspec/path/env edges (C++/Python) | matchspec/path/env edge + tests |
| `sphinx-doc/sphinx` | 8004 | disclosure | Requires AI disclosure section; docutils/path/config edges — prefer code over docs farm | builder/path/config edge + tests |
| `conda/conda` | 7505 | disclosure | Generative AI allowed with human ownership; no autonomous agents; env/path/matchspec | env/path/matchspec edge + tests |
| `PyCQA/isort` | 6951 | silent | Import sorter; parse/path edges | import-parse/path edge + fixtures |
| `PyO3/maturin` | 5785 | silent | Rust→wheel build backend; path/PEP517 edges; sibling of PyO3 (which bans unsolicited AI PRs) — stay human-shaped | PEP517/path/sdist edge + cargo tests |
| `pylint-dev/pylint` | 5722 | silent | Linter; AST/config/path edges; AGENTS.md guidance only | AST/config/path edge + functional tests |
| `pypa/virtualenv` | 5045 | silent | Venv builder; path/seed/discovery edges; tox-dev adjacent maintainers | path/seed/discovery edge + tests |
| `tox-dev/tox` | 3931 | silent | Prior scout: excellent outsider config/path/quoting merges; empty issue tracker — self-found tested hunks only | config/factor/path/set_env quoting + regression tests |
| `pantsbuild/pants` | 3826 | silent | Build system; goal/path/env edges; AGENTS guidance | path/env/goal parse edge + tests |
| `PyCQA/flake8` | 3822 | silent | Linter glue; plugin/path/config edges | plugin/config/path edge + tests |
| `copier-org/copier` | 3560 | disclosure | Explicit AI_POLICY: human-in-loop; no AI review comments; template path/render class | template path/render/update edge + tests |
| `coveragepy/coveragepy` | 3411 | silent | Coverage tool; path/trace/config edges | path/config/trace edge + tests |
| `beeware/briefcase` | 3347 | disclosure | App packaging; path/template/platform edges; BeeWare AI rules | template/path/platform edge + tests |
| `pypa/flit` | 2252 | silent | Simple packaging backend; metadata/path edges; quiet queue | metadata/path backend edge + tests |
| `pypa/twine` | 1788 | silent | PyPI upload utility; URL/path/config edges | config/URL/path edge + tests |
| `wntrblm/nox` | 1554 | silent | Session runner; path/env/posargs quoting class like tox | posargs/env/path quoting + tests |

### Tier notes

**Best first homes (small testable path/quoting/config hunks):**

1. `tox-dev/tox` — prior scout: outsider config/factor/`set_env` path/quoting merges; issue tracker empty → self-found tested hunks only; do not duplicate open UNC/extras PRs.
2. `wntrblm/nox` / `pypa/virtualenv` / `pypa/pipx` — same env/path/posargs class as tox, quieter.
3. `pallets/click` + `fastapi/typer` — CLI option/quoting parse with strong tests.
4. `pyenv/pyenv` — shell shim/PATH/quoting (CLI systems adjacent).
5. `HypothesisWorks/hypothesis` / `coveragepy/coveragepy` / `pytest-dev/pytest` — test infra; pytest requires human oversight (no purely agentic PRs) + AI credit.
6. `python-poetry/poetry` / `pdm-project/pdm` / `psf/black` — packaging/formatter; copy outsider PR voice.
7. `copier-org/copier` / `cookiecutter/cookiecutter` — template path/render; copier has explicit AI_POLICY (no AI review comments).
8. `conda/conda` / `mamba-org/mamba` — env/matchspec/path; conda generative-AI section is usable if human-owned.

**Careful / later:**

- `astral-sh/uv`, `astral-sh/ruff` — astral `AI_POLICY.md`: AI OK with human-in-loop; **no autonomous agents**; do not AI-write maintainer comments; high bar. Viable only with careful human voice — not a first-home pick.
- `sphinx-doc/sphinx`, `Nuitka/Nuitka`, `beeware/briefcase` — disclosure OK; prefer product-code hunks over docs.
- `PyO3/maturin` — good packaging surface; sibling `PyO3/pyo3` bans unsolicited AI PRs — stay strictly human-shaped.

**Park (scored leave for now):** `pypa/pip`, `psf/requests`, `hynek/structlog` (harsh DoS-by-slop LLM policies); `python/cpython` (too large for new account first home); `prefix-dev/pixi` (predecessor open queue).

## LEAVE list

| Repo | ★ | Policy | Reason |
|---|---:|---|---|
| `public-apis/public-apis` | 477229 | silent | Awesome API list — not product tooling |
| `EbookFoundation/free-programming-books` | 396232 | silent | Book list — not product |
| `donnemartin/system-design-primer` | 368649 | silent | Interview primer — not tooling product |
| `vinta/awesome-python` | 319202 | silent | Awesome list — not product |
| `practical-tutorials/project-based-learning` | 282532 | silent | Tutorial list — not product |
| `NousResearch/hermes-agent` | 243172 | silent | AI agent app — not python tooling |
| `yt-dlp/yt-dlp` | 189745 | hard_ban | CONTRIBUTING NO AI/NO LLM for issues, PRs, comments, translations |
| `Significant-Gravitas/AutoGPT` | 187195 | silent | AI agent — not tooling |
| `microsoft/markitdown` | 180949 | silent | Doc-conversion AI tool from noisy raw dump — weak playbook hunk class |
| `huggingface/transformers` | 164979 | silent | ML framework — wrong sector |
| `langchain-ai/langchain` | 145915 | silent | Agent platform — wrong sector |
| `fastapi/fastapi` | 102186 | hostility_risk | maybe-ai bot; hallucinated vuln farm risk |
| `django/django` | 90393 | hostility_risk | Required AI disclosure + docs-farm closes in playbook |
| `python/cpython` | 76471 | disclosure | Allows AI with human ownership but huge/high bar — not a first home for new account |
| `docling-project/docling` | 66141 | silent | GenAI document prep — docs/feature farm risk |
| `psf/requests` | 54293 | disclosure | Same harsh LLM policy as pip; DoS-by-slop permanent ban risk |
| `python/mypy` | 20633 | hostility_risk | Discourages LLM use by *new* contributors; mostly-LLM PRs closed |
| `aio-libs/aiohttp` | 16543 | agentscan | AgentScan adopter circle |
| `PyO3/pyo3` | 16116 | hard_ban | PR template: do not submit unsolicited AI-generated PRs |
| `pre-commit/pre-commit` | 15564 | hostility_risk | Maintainer closes genuine fixes as ai slop |
| `encode/httpx` | 15468 | silent | Issues disabled — hard to find labeled bugs |
| `sqlalchemy/sqlalchemy` | 12147 | hostility_risk | Asks not to spam AI/LLM content onto tracker |
| `pypa/pip` | 10278 | disclosure | Harsh PSF-style LLM policy (DoS-by-slop ban, no agentic); foundational — park for later |
| `jazzband/pip-tools` | 8007 | hostility_risk | Jazzband winding down after AI flood; LLM contrib discouraged |
| `prefix-dev/pixi` | 7696 | disclosure | Predecessor open queue (pixi CA) in CATALOG — do not steal |
| `pypa/hatch` | 7236 | hostility_risk | Predecessor open queue / outdated-thread lesson — do not steal |
| `mesonbuild/meson` | 6625 | hostility_risk | Predecessor open queue — do not steal |
| `hynek/structlog` | 4945 | disclosure | Same harsh LLM policy family; DoS-by-slop ban; small library |
| `pypa/setuptools` | 2857 | hostility_risk | Predecessor closed #5324 wrong tree — forever out |
| `pypa/cibuildwheel` | 2261 | hostility_risk | Predecessor closed #2979; open #2978 — do not steal |
| `pypa/build` | 855 | hostility_risk | Predecessor closed #1179 — forever out |
| `pypa/packaging` | 746 | silent | <1000★ (746) — repo-gate leave |
| `pypa/wheel` | 572 | hostility_risk | Satellite — forever out |
| `scikit-build/scikit-build-core` | 509 | hostility_risk | Predecessor home + <1000★ gate |
| `pypa/installer` | 148 | hostility_risk | Satellite — forever out |
| `pypa/distutils` | 59 | hostility_risk | Satellite 59★ — forever out |

## Sector synthesis

- **Raw input is noisy:** top of `python-tooling.jsonl` is awesome-lists / AI agents / ML apps. Real tooling was curated from known ecosystems (pytest/tox/astral/pypa/PyCQA/…) plus adjacent libraries.
- **Hard bans in-sector:** `yt-dlp` (Zig-style NO AI/LLM everywhere) and `PyO3/pyo3` (no unsolicited AI PRs). Leave both.
- **Predecessor wall:** never re-enter `build`/`setuptools`/`distutils`/`wheel`/`installer`/`cibuildwheel`/`hatch`; also do not steal `meson` / `scikit-build-core` / `pixi` open queues.
- **AgentScan:** `aio-libs/aiohttp` only in this sample — leave the circle.
- **Fit theme:** tox/nox/virtualenv/pipx env+path+quoting; click/typer CLI parse; poetry/pdm/flit/twine packaging metadata/path; black/ruff parse fixtures; pyenv shims; hypothesis/coverage/pytest test infra.
- **Avoid:** awesome dumps; AutoGPT/langchain-class agents; FastAPI/Django docs+maybe-ai farms; Jazzband/pre-commit hostility; satellites under 1k★.

## Method notes

- Policy files probed via GitHub GraphQL blob reads (REST core rate-limit exhausted mid-survey): CONTRIBUTING*, AI.md, AI_POLICY.md, AGENTS.md, PR templates, workflow names.
- Local AgentScan adopters/skip_orgs check (no `--refresh` during survey).
- Prior scout (`oss-scout-candidates.md`) reused for pytest/tox/ruff/uv/pre-commit/httpx notes.
- No forks, PRs, or tracker comments.
