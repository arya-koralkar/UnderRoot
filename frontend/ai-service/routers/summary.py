from fastapi import APIRouter
from models.schemas import SummaryRequest, SummaryResponse, SectionSummary
from services.summarizer import _split_sections, summarize_section, draft_abstract

router = APIRouter()


@router.post("/generate", response_model=SummaryResponse)
async def generate_summary(request: SummaryRequest):
    sections = _split_sections(request.text)
    section_summaries = []
    for title, content in sections:
        if content.strip():
            summary = summarize_section(title, content)
            section_summaries.append(SectionSummary(title=title, summary=summary))

    abstract = draft_abstract(request.text)

    return SummaryResponse(
        section_summaries=section_summaries,
        abstract_draft=abstract,
    )
