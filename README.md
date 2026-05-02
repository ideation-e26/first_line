# First line

## What is it?
MVP for a pre-triage and booking service

## Dev run app
```
uvicorn app.main:app --reload
```

## Dev setup
1. In VS Code, install the `Dev Container` extension
2. Open Command Palet (`cmd + shift + p`) -> `Dev Containers: Rebuild Container`
3. In VS Code install all the `python` extensions
3. Create your `.env` and put your API keys

## CI

The CI runs automatically on pull requests and on pushes to `main`.

It checks:
- dependencies install with `uv`
- formatting with Ruff
- linting with Ruff
- tests with pytest
- Docker image build

To run the same checks locally:
```bash
uv sync --locked --dev
uv run ruff format --check .
uv run ruff check .
uv run pytest
docker build -t first-line-app .
```
To fix formatting/lint issues:
```
uv run ruff format .
uv run ruff check . --fix
```
