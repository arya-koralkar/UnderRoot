from typing import List, Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from config import SEMANTIC_SCHOLAR_API_KEY

_SS_BASE = "https://api.semanticscholar.org/graph/v1"
_SS_FIELDS = "paperId,title,authors,year,venue,citationCount,externalIds,abstract"


def extract_keywords(claim: str, top_n: int = 5) -> str:
    """Extract key terms from a claim using TF-IDF."""
    try:
        vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n)
        vectorizer.fit_transform([claim])
        return " ".join(vectorizer.get_feature_names_out())
    except Exception:
        return claim[:100]


def search_papers(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Query Semantic Scholar for papers matching the query."""
    headers = {}
    if SEMANTIC_SCHOLAR_API_KEY:
        headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY

    try:
        resp = requests.get(
            f"{_SS_BASE}/paper/search",
            params={"query": query, "limit": limit, "fields": _SS_FIELDS},
            headers=headers,
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json().get("data", [])
    except Exception:
        return []


def search_for_claim(claim: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Extract keywords from claim and search Semantic Scholar."""
    keywords = extract_keywords(claim)
    return search_papers(keywords, limit=limit)
