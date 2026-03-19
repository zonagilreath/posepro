# PosePro

AI-powered proposal writer for freelancers.

PosePro turns client briefs into structured proposal drafts with support for streaming generation, editing, templates, and export workflows. The app is being built with a FastAPI backend and a React frontend, with AI-assisted proposal generation as the core product experience.

## Overview

The repository is organized around the main product areas:

- backend APIs for auth, briefs, proposals, generation, and export flows
- data models for users, briefs, proposals, and templates
- streaming proposal generation for real-time UI updates
- frontend surfaces for brief intake, dashboard views, editing, and proposal review

## Structure

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

## Tech stack

### Backend

- Python 3.11+
- FastAPI
- SQLAlchemy
- Poetry
- Pydantic

### Frontend

- React
- TypeScript
- Vite

### Integrations

- Claude API for proposal generation
- Supabase / PostgreSQL for persistence and auth

## Setup

### Clone the repository

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

### Backend

Poetry’s documentation recommends `pipx install poetry` as the installation path for Poetry ([Poetry docs](https://python-poetry.org/docs/)).

Unix/macOS:

```bash
cd backend
cp .env.example .env
poetry install
```

Windows PowerShell:

```powershell
cd backend
Copy-Item .env.example .env
poetry install
```

### Frontend

Unix/macOS:

```bash
cd ../frontend
cp .env.example .env
npm install
```

Windows PowerShell:

```powershell
cd ..\frontend
Copy-Item .env.example .env
npm install
```

## Running locally

Run backend and frontend in separate terminals.

### Backend

The backend runs with `uvicorn app.main:app --reload`. FastAPI documents `StreamingResponse` and SSE-style streaming patterns for real-time responses, which are relevant for the proposal generation flow ([FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)), ([FastAPI SSE docs](https://fastapi.tiangolo.com/tutorial/server-sent-events/)).

Unix/macOS:

```bash
cd backend
poetry run uvicorn app.main:app --reload
```

Windows PowerShell:

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

### Frontend

Vite’s guide uses the `react-ts` template for React + TypeScript projects ([Vite guide](https://vite.dev/guide/)).

Unix/macOS:

```bash
cd frontend
npm run dev
```

Windows PowerShell:

```powershell
cd frontend
npm run dev
```

Frontend URL:

- App: `http://localhost:5173`

## Environment variables

### `backend/.env`

- `APP_NAME`
- `APP_ENV`
- `API_PREFIX`
- `CORS_ORIGINS`
- `DATABASE_URL`
- `SQLALCHEMY_ECHO`
- `ANTHROPIC_API_KEY`

The local default uses SQLite so the backend can run without provisioning Postgres first.

### `frontend/.env`

- `VITE_API_BASE_URL`

## API surface

### Auth

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/session`

### Proposal generation

- `POST /api/proposals/generate/preview`
- `POST /api/proposals/generate`

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

## Product areas

Current focus areas include:

- backend CRUD and validation
- auth flows and session handling
- brief intake and dashboard views
- proposal editing, templates, and export
- real-time streaming generation UX
