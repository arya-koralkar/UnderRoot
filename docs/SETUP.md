# UnderRoot — Setup Guide

## Prerequisites

| Tool | Version |
|------|---------|
| Docker | 24+ |
| Docker Compose | 2.20+ |
| Node.js | 18+ |
| Python | 3.11+ |
| Git | 2.40+ |

## API Keys Required

| Key | Where to Get |
|-----|-------------|
| `GEMINI_API_KEY` | [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `SEMANTIC_SCHOLAR_API_KEY` | [Semantic Scholar](https://www.semanticscholar.org/product/api) |
| `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` | [Google Cloud Console](https://console.cloud.google.com/) |
| `JWT_SECRET` | Generate with `openssl rand -hex 32` |

## Docker Quick Start

```bash
git clone https://github.com/diMo2004/UnderRoot.git
cd UnderRoot
cp .env.example .env
# Edit .env with your API keys
docker-compose up --build
```

Services will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:4000
- Collaboration: ws://localhost:4001
- AI Service: http://localhost:8000

## Manual Setup

### 1. PostgreSQL, MongoDB, Redis

Start infrastructure services only:
```bash
docker-compose up postgres mongo redis -d
```

### 2. Backend

```bash
cd backend
npm install
cp ../.env.example .env
# Edit .env
npm run dev
```

### 3. AI Service

```bash
cd ai-service
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example .env
# Edit .env
uvicorn main:app --reload --port 8000
```

### 4. Frontend

```bash
cd frontend
npm install
cp ../.env.example .env.local
# Set NEXT_PUBLIC_BACKEND_URL=http://localhost:4000
# Set NEXT_PUBLIC_COLLAB_URL=ws://localhost:4001
npm run dev
```

## Team Vaultron

| Name | Role | Responsibilities |
|------|------|-----------------|
| Team Vaultron | Full-Stack & AI | All components |
