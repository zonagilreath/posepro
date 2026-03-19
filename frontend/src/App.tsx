import { useEffect, useState } from 'react'

type HealthResponse = {
  status?: string
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export function App() {
  const [health, setHealth] = useState<'loading' | 'ok' | 'error'>('loading')

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/health`)
      .then((response) => {
        if (!response.ok) throw new Error('Request failed')
        return response.json() as Promise<HealthResponse>
      })
      .then((data) => setHealth(data.status === 'ok' ? 'ok' : 'error'))
      .catch(() => setHealth('error'))
  }, [])

  return (
    <main className="page-shell">
      <section className="card">
        <p className="eyebrow">PosePro</p>
        <h1>Starter scaffold</h1>
        <p className="body-copy">
          Minimal frontend and backend structure based on the current project brief.
        </p>
        <div className="status-row">
          <span className="label">API health</span>
          <span className={`badge badge-${health}`}>{health}</span>
        </div>
        <ul className="checklist">
          <li>backend/app for FastAPI routes, config, models, services</li>
          <li>frontend/src for the React app shell</li>
          <li>.env example and onboarding docs ready for the next pass</li>
        </ul>
      </section>
    </main>
  )
}
