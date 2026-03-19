# PosePro

Minimal starter scaffold for the PosePro project.

This repo is intentionally small. It gives you a clean split between backend and frontend, confirms the two sides can talk to each other, and leaves the actual product work open instead of locking you into premature architecture.

## What is included

- `backend/` — FastAPI app with config loading, CORS setup, and a health route
- `backend/app/config/` — environment-driven settings
- `backend/app/routers/` — API route modules
- `backend/app/models/` — placeholder for SQLAlchemy models
- `backend/app/services/` — placeholder for AI, auth, and business logic
- `frontend/` — Vite + React + TypeScript app
- `frontend/src/App.tsx` — simple app shell with a backend health check
- `.env.example` files for backend and frontend

## Why this structure

The attached project brief points toward a FastAPI backend with `app/routers`, `app/models`, `app/services`, and `app/config`, plus a React frontend using Vite and TypeScript. The repo follows that shape, but stops short of implementing the real features so you can make those decisions incrementally.

The backend is ready for adding auth, SQLAlchemy models, proposal generation services, and SSE routes from the brief. The frontend is ready for auth screens, dashboard work, the brief intake form, and the streaming proposal UI described in the brief.

## Current layout

```text
posepro/
├── backend/
│   ├── app/
│   │   ├── config/
│   │   │   └── settings.py
│   │   ├── models/
│   │   ├── routers/
│   │   │   └── health.py
│   │   ├── services/
│   │   └── main.py
│   ├── .env.example
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── styles.css
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

The project brief explicitly expects `uvicorn app.main:app --reload` as the dev server command. FastAPI’s current docs also document `fastapi dev` as a recommended development entry point ([FastAPI docs](https://fastapi.tiangolo.com/)). This scaffold keeps the brief-aligned `uvicorn` command.

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
- `ANTHROPIC_API_KEY`

### `frontend/.env`

Current fields:

- `VITE_API_BASE_URL`

## Suggested next steps

Based on the project brief, the next sensible slices are:

- add SQLAlchemy base setup and initial models for `User`, `Brief`, `Proposal`, and `Template`
- add auth route stubs and middleware
- add proposal generation service interfaces without fully implementing the prompt chain yet
- add a brief submission form in the frontend
- add an SSE endpoint contract before building the streaming UI

## Notes on sources

I attempted to inspect the live Linear PosePro project directly, but the current Linear connector required reauthentication and the local browser session was not signed in during review. The repo scaffold therefore follows the attached project brief and the target stack it defines.
