from fastapi import APIRouter
from models.schemas import CitationRequest, CitationResponse
from services.claim_detector import detect_claims
from services.citation_search import search_for_claim
from services.citation_ranker import rank_papers
from services.citation_formatter import normalize_paper

router = APIRouter()


@router.post("/suggest", response_model=CitationResponse)
async def suggest_citations(request: CitationRequest):
    claims = detect_claims(request.text)

    all_papers: dict = {}
    for claim in claims[:5]:  # Limit to top 5 claims for performance
        raw_papers = search_for_claim(claim, limit=10)
        ranked = rank_papers(claim, raw_papers)
        for paper in ranked[:5]:
            pid = paper.get("paperId", "")
            if pid and pid not in all_papers:
                all_papers[pid] = paper

    normalized = [normalize_paper(p) for p in list(all_papers.values())[:10]]
    # Re-sort by relevance_score descending
    normalized.sort(key=lambda x: x["relevance_score"], reverse=True)

    return CitationResponse(citations=normalized, claims_detected=claims)
