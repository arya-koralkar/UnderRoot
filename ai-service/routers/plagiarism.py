import re
from datetime import datetime, timezone
from fastapi import APIRouter
from models.schemas import PlagiarismRequest, PlagiarismResponse
from services.plagiarism_lexical import check_lexical
from services.plagiarism_semantic import check_semantic
from services.plagiarism_structural import check_structural
from services.plagiarism_aggregator import build_section_result, aggregate_scores

router = APIRouter()

_HEADING_RE = re.compile(
    r"^(abstract|introduction|related work|methodology|results|discussion|conclusion)",
    re.IGNORECASE,
)


def _split_sections(text: str):
    """Split text into (section_title, sentences) pairs."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    sections = []
    current_title = "Document"
    current_sentences: list = []

    for para in paragraphs:
        first_line = para.split("\n")[0].strip()
        if _HEADING_RE.match(first_line) and len(first_line) < 60:
            if current_sentences:
                sections.append((current_title, current_sentences))
            current_title = first_line
            current_sentences = []
        else:
            sentences = re.split(r"(?<=[.!?])\s+", para)
            current_sentences.extend([s.strip() for s in sentences if s.strip()])

    if current_sentences:
        sections.append((current_title, current_sentences))

    return sections if sections else [("Document", [text])]


# Placeholder reference corpus — in production this would be retrieved per-document
_REFERENCE_CORPUS = [
    "Machine learning is a subfield of artificial intelligence.",
    "Deep learning models require large amounts of training data.",
    "Neural networks are inspired by the human brain.",
]


@router.post("/check", response_model=PlagiarismResponse)
async def check_plagiarism(request: PlagiarismRequest):
    sections = _split_sections(request.text)
    section_results = []

    for title, sentences in sections:
        if not sentences:
            continue
        lex = check_lexical(sentences, _REFERENCE_CORPUS)
        sem = check_semantic(sentences, _REFERENCE_CORPUS)
        struct = check_structural(sentences, _REFERENCE_CORPUS)
        section_results.append(build_section_result(title, sentences, lex, sem, struct))

    if section_results:
        overall = sum(s["overall_score"] for s in section_results) / len(section_results)
    else:
        overall = 0.0

    severities = {"low": 0, "moderate": 1, "high": 2, "critical": 3}
    rev_severities = {v: k for k, v in severities.items()}
    max_sev = max((severities.get(s["severity"], 0) for s in section_results), default=0)

    if overall < 0.15:
        sev_label = "low"
    elif overall < 0.25:
        sev_label = "moderate"
    elif overall < 0.40:
        sev_label = "high"
    else:
        sev_label = "critical"

    return PlagiarismResponse(
        overall_score=round(overall, 4),
        severity=sev_label,
        sections=section_results,
        checked_at=datetime.now(timezone.utc).isoformat(),
    )
