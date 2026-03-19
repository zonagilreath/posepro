# PosePro

AI-powered proposal writer for freelancers.

PosePro is a full-stack application for turning client briefs into structured proposal drafts with support for streaming generation, editing, templates, and export workflows. The current project direction in Linear centers on a FastAPI backend, a React frontend, and Claude-powered proposal generation ([PosePro project](https://linear.app/zonadostuff/project/posepro-61e2edef5fc9)).

## Overview

The repository is organized around the main product areas already defined in the project work:

- FastAPI backend for auth, briefs, proposals, generation, and export flows ([ZON-5](https://linear.app/zonadostuff/issue/ZON-5/fastapi-project-setup)), ([ZON-7](https://linear.app/zonadostuff/issue/ZON-7/crud-endpoints-for-briefs-and-proposals)), ([ZON-8](https://linear.app/zonadostuff/issue/ZON-8/auth-integration))
- SQLAlchemy models for users, briefs, proposals, and templates ([ZON-6](https://linear.app/zonadostuff/issue/ZON-6/database-models-with-sqlalchemy))
- structured proposal generation and streaming delivery to the frontend ([ZON-9](https://linear.app/zonadostuff/issue/ZON-9/ai-proposal-generation-structured-prompting)), ([ZON-10](https://linear.app/zonadostuff/issue/ZON-10/streaming-sse-endpoint-for-generation))
- React frontend for the brief intake flow, dashboard, editor, and generation view ([ZON-14](https://linear.app/zonadostuff/issue/ZON-14/react-project-setup)), ([ZON-17](https://linear.app/zonadostuff/issue/ZON-17/brief-input-form)), ([ZON-18](https://linear.app/zonadostuff/issue/ZON-18/streaming-generation-view))

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

### Planned platform integrations

- Claude API for proposal generation ([ZON-9](https://linear.app/zonadostuff/issue/ZON-9/ai-proposal-generation-structured-prompting))
- Supabase / PostgreSQL for persistence and auth ([ZON-6](https://linear.app/zonadostuff/issue/ZON-6/database-models-with-sqlalchemy)), ([ZON-8](https://linear.app/zonadostuff/issue/ZON-8/auth-integration))

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

The backend currently uses `uvicorn app.main:app --reload`, which matches the FastAPI setup direction already defined for the project ([ZON-5](https://linear.app/zonadostuff/issue/ZON-5/fastapi-project-setup)). FastAPI documents `StreamingResponse` and SSE-style streaming patterns for real-time responses, which is relevant for the proposal generation flow ([FastAPI custom responses](https://fastapi.tiangolo.com/advanced/custom-response/)), ([FastAPI SSE docs](https://fastapi.tiangolo.com/tutorial/server-sent-events/)).

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

These routes match the auth work tracked in Linear ([ZON-8](https://linear.app/zonadostuff/issue/ZON-8/auth-integration)).

### Proposal generation

- `POST /api/proposals/generate/preview`
- `POST /api/proposals/generate`

The proposal generation endpoints map to the structured prompting and streaming work tracked in Linear ([ZON-9](https://linear.app/zonadostuff/issue/ZON-9/ai-proposal-generation-structured-prompting)), ([ZON-10](https://linear.app/zonadostuff/issue/ZON-10/streaming-sse-endpoint-for-generation)).

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

## Roadmap areas

Current work in Linear covers:

- backend CRUD and validation ([ZON-7](https://linear.app/zonadostuff/issue/ZON-7/crud-endpoints-for-briefs-and-proposals)), ([ZON-13](https://linear.app/zonadostuff/issue/ZON-13/error-handling-and-input-validation))
- frontend auth, dashboard, and brief intake ([ZON-15](https://linear.app/zonadostuff/issue/ZON-15/auth-flow-ui)), ([ZON-16](https://linear.app/zonadostuff/issue/ZON-16/dashboard-page)), ([ZON-17](https://linear.app/zonadostuff/issue/ZON-17/brief-input-form))
- editor, templates, export, and presentation polish ([ZON-19](https://linear.app/zonadostuff/issue/ZON-19/rich-text-editor-integration)), ([ZON-21](https://linear.app/zonadostuff/issue/ZON-21/template-library-page)), ([ZON-22](https://linear.app/zonadostuff/issue/ZON-22/export-pdf-copy-shareable-link)), ([ZON-23](https://linear.app/zonadostuff/issue/ZON-23/landing-page))
