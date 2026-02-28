# 📝 UnderRoot

**An AI-Powered Real-Time Collaborative Research Paper Writing Tool — Write. Cite. Check. Collaborate.**

## Features

- ✍️ **Real-Time Collaboration** — Multiple authors edit simultaneously via Yjs + HocusPocus CRDT
- 🔍 **AI Citation Suggestions** — Claim detection + Semantic Scholar search + semantic ranking
- 🛡️ **Plagiarism Detection** — Three-layer analysis: lexical, semantic, and structural
- 📄 **Smart Summaries** — Gemini-powered section summaries and abstract drafts
- 📤 **Export** — Download as PDF, DOCX, or LaTeX
- 👥 **Presence Awareness** — See collaborators' cursors and avatars in real time

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 15, Tiptap, Yjs, Tailwind CSS, Zustand |
| Collaboration | HocusPocus, Yjs CRDT, WebSocket |
| Backend | Node.js, Express, JWT, PostgreSQL, MongoDB, Redis |
| AI Service | Python, FastAPI, Gemini 1.5 Flash, Sentence-Transformers, FAISS |
| Search | Semantic Scholar API, TF-IDF, all-MiniLM-L6-v2 |
| Plagiarism | TF-IDF (lexical) + FAISS (semantic) + SimHash (structural) |
| Infrastructure | Docker, Docker Compose |

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local dev)
- Python 3.11+ (for local dev)

### Using Docker (Recommended)

```bash
git clone https://github.com/diMo2004/UnderRoot.git
cd UnderRoot
cp .env.example .env
# Fill in API keys in .env
docker-compose up --build
```

Open [http://localhost:3000](http://localhost:3000)

### Manual Setup

See [docs/SETUP.md](docs/SETUP.md) for detailed instructions.

## Team Vaultron

| Name | Role |
|------|------|
| Team Vaultron | Full-Stack & AI Development |

## License

MIT
