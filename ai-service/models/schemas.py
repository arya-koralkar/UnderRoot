from pydantic import BaseModel
from typing import List, Optional


# Citation schemas
class CitationRequest(BaseModel):
    text: str
    project_id: Optional[str] = None


class Paper(BaseModel):
    paper_id: str
    title: str
    authors: List[str]
    year: int
    venue: str
    citation_count: int
    relevance_score: float
    doi: Optional[str] = None
    url: Optional[str] = None
    abstract: Optional[str] = None


class CitationResponse(BaseModel):
    citations: List[Paper]
    claims_detected: List[str]


# Plagiarism schemas
class PlagiarismRequest(BaseModel):
    text: str
    project_id: Optional[str] = None


class PlagiarismMatch(BaseModel):
    matched_text: str
    source: str
    similarity: float
    start_index: int
    end_index: int


class SectionPlagiarism(BaseModel):
    section_title: str
    overall_score: float
    severity: str  # low | moderate | high | critical
    matches: List[PlagiarismMatch]


class PlagiarismResponse(BaseModel):
    overall_score: float
    severity: str
    sections: List[SectionPlagiarism]
    checked_at: str


# Summary schemas
class SummaryRequest(BaseModel):
    text: str
    project_id: Optional[str] = None


class SectionSummary(BaseModel):
    title: str
    summary: str


class SummaryResponse(BaseModel):
    section_summaries: List[SectionSummary]
    abstract_draft: str
