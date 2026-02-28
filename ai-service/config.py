import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
SEMANTIC_SCHOLAR_API_KEY: str = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")
SBERT_MODEL: str = "paraphrase-MiniLM-L12-v2"
RANKING_MODEL: str = "all-MiniLM-L6-v2"
