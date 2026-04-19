<<<<<<< HEAD
import os
=======
>>>>>>> ai-service-fix
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import citation, plagiarism, summary

app = FastAPI(
    title="UnderRoot AI Service",
    version="0.1.0",
    description="AI-powered citation suggestions, plagiarism detection, and summarization for UnderRoot.",
)

<<<<<<< HEAD
allowed_origins = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
=======
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
>>>>>>> ai-service-fix
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(citation.router, prefix="/api/citations", tags=["citations"])
app.include_router(plagiarism.router, prefix="/api/plagiarism", tags=["plagiarism"])
app.include_router(summary.router, prefix="/api/summary", tags=["summary"])

<<<<<<< HEAD
@app.get("/health")
def health():
    return {"status": "ok", "service": "underroot-ai-service"}
=======

@app.get("/health")
def health():
    return {"status": "ok", "service": "underroot-ai-service"}
>>>>>>> ai-service-fix
