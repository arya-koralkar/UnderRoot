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
<<<<<<< HEAD
class PlagiarismRequest(BaseModel):
    text: str
    project_id: Optional[str] = None


class PlagiarismMatch(BaseModel):
    matched_text: str
    source: str
    similarity: float
    start_index: int
    end_index: int
=======
>>>>>>> ai-service-fix


class SectionPlagiarism(BaseModel):
    section_title: str
    overall_score: float
    severity: str  # low | moderate | high | critical
    matches: List[PlagiarismMatch]


<<<<<<< HEAD
class PlagiarismResponse(BaseModel):
    overall_score: float
    severity: str
    sections: List[SectionPlagiarism]
    checked_at: str


=======
>>>>>>> ai-service-fix
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
<<<<<<< HEAD
=======

class SourceEvidence(BaseModel):
    title: Optional[str] = None
    url: Optional[str] = None
    doi: Optional[str] = None
    year: Optional[int] = None
    provider: Optional[str] = None


class PlagiarismMatch(BaseModel):
    matched_text: str
    source: SourceEvidence | str
    similarity: float
    start_index: int
    end_index: int
    source_index: Optional[int] = None
    source_text: Optional[str] = None
    source_layer: Optional[str] = None
    candidate_source_indices: Optional[List[int]] = None
    top_sources: Optional[List[SourceEvidence]] = None


class PlagiarismSection(BaseModel):
    section_title: str
    overall_score: float
    severity: str
    matches: List[PlagiarismMatch]


class PlagiarismRequest(BaseModel):
    text: str
    use_scholarly_sources: bool = True
    per_source_limit: int = 15


class PlagiarismResponse(BaseModel):
    overall_score: float
    severity: str
    sections: List[PlagiarismSection]
    checked_at: str
>>>>>>> ai-service-fix
