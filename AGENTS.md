# Repository Guidelines

> response in 中文, 保留英文的计算机术语，像技术Geek一样交流!
> 避免过度设计, 保持简洁实用和优雅的系统设计风格和代码风格!

## Project Structure & Module Organization
- `backend/` – FastAPI app (SQLModel, Alembic). Code in `backend/app/`; tests in `backend/tests/`; helper scripts in `backend/scripts/`.
- `frontend/` – Vite + React + TypeScript. App in `frontend/src/`; e2e tests in `frontend/tests/`; generated API client in `frontend/src/client/`.
- `scripts/` – repo-level helpers (build, test, client generation). Stack config in `docker/docker-compose*.yml`; environment in module-specific `.env` files.

## Build, Test, and Development Commands
- Start full stack (watch/reload): `docker compose -f docker/docker-compose.yml watch`
- Backend local dev: `cd backend && uv sync && source .venv/bin/activate && fastapi dev app/main.py`
- Backend lint/format: `cd backend && bash scripts/lint.sh` and `bash scripts/format.sh`
- Backend tests + coverage: `cd backend && bash scripts/test.sh`
- Frontend dev: `cd frontend && npm install && npm run dev`
- Frontend e2e (backend up): `cd frontend && npx playwright test`
- Generate API client: `./scripts/generate-client.sh`

## Coding Style & Naming Conventions
- Python: Ruff (lint/format) + MyPy (strict). 4‑space indent. Type hints required. `snake_case` for functions/vars, `PascalCase` for classes. Place APIs under `backend/app/api`, models in `models.py`, CRUD in `crud.py`.
- Frontend: Biome (`npm run lint`) for lint/format. React components `PascalCase` in `src/components`, routes in `src/routes`. Use TypeScript, `camelCase` for variables/props.

## Testing Guidelines
- Backend: Pytest in `backend/tests`. Name tests like `test_<module>.py`. Coverage HTML at `backend/htmlcov/index.html`.
- Frontend: Playwright specs in `frontend/tests/*.spec.ts`; helpers in `frontend/tests/utils`.

## Commit & Pull Request Guidelines
- Use concise, descriptive messages; conventional style with emojis is common (e.g., 🐛 fix, 📝 docs, ⬆ bump).
- PRs must include: clear description, linked issues, tests (or rationale), updated docs, and pass pre-commit/CI. Add screenshots/GIFs for UI changes.

## Security & Configuration Tips
- Don't commit secrets. Manage configuration in module-specific `.env` files (docker/.env, backend/.env, frontend/.env); rotate keys when sharing. Use the .env.example templates to get started.

## Agent-Specific Instructions
- Keep changes minimal and localized; follow existing structure and scripts.
- Install hooks and preflight locally: `uv run pre-commit install` then `uv run pre-commit run --all-files`.

