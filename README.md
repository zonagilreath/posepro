# PosePro

Minimal starter scaffold for the PosePro project.

This repo is intentionally small, but it now includes a thin backend slice for the next real Linear work: SQLAlchemy model stubs, auth route stubs, and a structured proposal preview plus SSE stream endpoint.

## What is included

- `backend/` — FastAPI app with config loading, CORS setup, auth routes, proposal routes, and a health route
- `backend/app/config/` — environment-driven settings
- `backend/app/db/` — shared SQLAlchemy engine and session setup
- `backend/app/models/` — thin SQLAlchemy models for `User`, `Brief`, `Proposal`, and `Template`
- `backend/app/routers/` — route modules for health, auth, and proposal generation
- `backend/app/schemas/` — Pydantic request and response models
- `backend/app/services/` — stubbed auth and proposal-generation service layer
- `frontend/` — Vite + React + TypeScript app
- `frontend/src/App.tsx` — simple app shell with a backend health check
- `.env.example` files for backend and frontend

## Why this structure

The repo shape now lines up with the live PosePro Linear work for FastAPI setup, SQLAlchemy models, auth integration, structured proposal generation, and the SSE hero flow ([ZON-5](https://linear.app/zonadostuff/issue/ZON-5/fastapi-project-setup)), ([ZON-6](https://linear.app/zonadostuff/issue/ZON-6/database-models-with-sqlalchemy)), ([ZON-8](https://linear.app/zonadostuff/issue/ZON-8/auth-integration)), ([ZON-9](https://linear.app/zonadostuff/issue/ZON-9/ai-proposal-generation-structured-prompting)), ([ZON-10](https://linear.app/zonadostuff/issue/ZON-10/streaming-sse-endpoint-for-generation)).

The backend still stops short of real persistence, real auth, and real Claude integration. That keeps the project easy to reshape while still giving you the correct route surface area and data contracts to build against.

## Current layout

```text
posepro/
├── backend/
│   ├── app/
│   │   ├── config/
│   │   │   └── settings.py
│   │   ├── db/
│   │   │   └── session.py
│   │   ├── models/
│   │   │   ├── base.py
│   │   │   ├── brief.py
│   │   │   ├── proposal.py
│   │   │   ├── template.py
│   │   │   └── user.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── health.py
│   │   │   └── proposals.py
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   └── proposals.py
│   │   ├── services/
│   │   │   ├── auth.py
│   │   │   └── proposal_generation.py
│   │   └── main.py
│   ├── .env.example
│   ├── poetry.lock
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── styles.css
│   │   └── vite-env.d.ts
│   ├── .env.example
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── .gitignore
├── package.json
└── README.md
```

## Dependencies

### Backend

Required:

- Python 3.11+
- Poetry

Current defaults:

- SQLite for local setup
- stubbed proposal generation service

Optional later, not yet wired:

- PostgreSQL / Supabase
- Anthropic API key

### Frontend

Required:

- Node.js 20+
- npm

## First-time setup

### 1. Clone the repo

Unix/macOS:

```bash
git clone https://github.com/zonagilreath/posepro.git
cd posepro
```

Windows PowerShell:

```powershell
git clone https://github.com/zonagilreath/posepro.git
cd posepro
```

### 2. Install backend dependencies

#### Unix/macOS

If Poetry is not installed yet, the official docs recommend `pipx install poetry` ([Poetry docs](https://python-poetry.org/docs/)).

```bash
cd backend
cp .env.example .env
poetry install
```

#### Windows PowerShell

If Poetry is not installed yet, install it with `pipx install poetry` per the official docs ([Poetry docs](https://python-poetry.org/docs/)).

```powershell
cd backend
Copy-Item .env.example .env
poetry install
```

### 3. Install frontend dependencies

#### Unix/macOS

```bash
cd ../frontend
cp .env.example .env
npm install
```

#### Windows PowerShell

```powershell
cd ..\frontend
Copy-Item .env.example .env
npm install
```

## Running the project

You run backend and frontend in separate terminals.

### Backend dev server

The project brief explicitly expects `uvicorn app.main:app --reload` as the dev server command. FastAPI’s docs also support streamed responses through `StreamingResponse`, and FastAPI documents SSE-style streaming patterns for real-time updates ([FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)), ([FastAPI SSE docs](https://fastapi.tiangolo.com/tutorial/server-sent-events/)).

#### Unix/macOS

```bash
cd backend
poetry run uvicorn app.main:app --reload
```

#### Windows PowerShell

```powershell
cd backend
poetry run uvicorn app.main:app --reload
```

Backend URLs:

- API root: `http://localhost:8000/`
- Health check: `http://localhost:8000/api/health`
- Swagger docs: `http://localhost:8000/docs`
- Auth routes: `http://localhost:8000/api/auth/*`
- Proposal preview: `POST http://localhost:8000/api/proposals/generate/preview`
- Proposal stream: `POST http://localhost:8000/api/proposals/generate`

### Frontend dev server

Vite’s current getting-started guide uses the `react-ts` template for React + TypeScript projects ([Vite guide](https://vite.dev/guide/)). This scaffold follows that basic setup.

#### Unix/macOS

```bash
cd frontend
npm run dev
```

#### Windows PowerShell

```powershell
cd frontend
npm run dev
```

Frontend URL:

- App: `http://localhost:5173`

If both servers are running, the frontend should show `API health: ok`.

## Environment files

### `backend/.env`

Current fields:

- `APP_NAME`
- `APP_ENV`
- `API_PREFIX`
- `CORS_ORIGINS`
- `DATABASE_URL`
- `SQLALCHEMY_ECHO`
- `ANTHROPIC_API_KEY`

Local default uses SQLite so you can boot the backend without provisioning Postgres first.

### `frontend/.env`

Current fields:

- `VITE_API_BASE_URL`

## Current backend contracts

### Auth

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/session`

These are stubbed and return fake dev tokens for now. They exist to lock in the contract from the Linear auth issue before wiring real Supabase Auth or JWT handling ([ZON-8](https://linear.app/zonadostuff/issue/ZON-8/auth-integration)).

### Proposal generation

- `POST /api/proposals/generate/preview`
- `POST /api/proposals/generate`

`/generate/preview` returns structured JSON sections. `/generate` returns a `text/event-stream` response that emits section events followed by a final complete event, matching the intended streaming UX from the Linear hero feature issues ([ZON-9](https://linear.app/zonadostuff/issue/ZON-9/ai-proposal-generation-structured-prompting)), ([ZON-10](https://linear.app/zonadostuff/issue/ZON-10/streaming-sse-endpoint-for-generation)).

Example preview request:

```json
{
  "brief_content": "Build a proposal tool for freelancers that can turn a pasted project brief into a polished draft.",
  "structured_fields": {
    "budget": "$3k-$5k",
    "timeline": "2-3 weeks",
    "industry": "SaaS"
  },
  "tone": "professional",
  "length": "concise"
}
```

## What is still intentionally thin

- no Alembic setup yet
- no real DB persistence or CRUD handlers yet
- no auth middleware yet
- no real Claude API integration yet
- no frontend wiring for auth, brief submission, or stream consumption yet

## Best next steps

The most natural next slice is:

- add Alembic and first migration shell for the four models
- add protected-route dependency and swap auth stubs toward real JWT or Supabase auth
- add brief and proposal CRUD route stubs to match the remaining backend issues
- wire the frontend brief form to the preview and stream endpoints
- replace the stub generation service with a real Claude-backed implementation
