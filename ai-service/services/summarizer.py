from typing import List
import re
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel("gemini-1.5-flash")


def _split_sections(text: str) -> List[tuple]:
    """Split text into (title, content) pairs."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    sections = []
    current_title = "Document"
    current_content: list = []

    heading_re = re.compile(
        r"^(abstract|introduction|related work|methodology|results|discussion|conclusion|\d+\.)",
        re.IGNORECASE,
    )

    for para in paragraphs:
        first_line = para.split("\n")[0].strip()
        if heading_re.match(first_line) and len(first_line) < 80:
            if current_content:
                sections.append((current_title, "\n".join(current_content)))
            current_title = first_line
            current_content = [para[len(first_line):].strip()]
        else:
            current_content.append(para)

    if current_content:
        sections.append((current_title, "\n".join(current_content)))

    return sections or [("Document", text)]


def summarize_section(title: str, content: str) -> str:
    prompt = (
        f"Summarize the following '{title}' section of a research paper in 2-3 concise sentences:\n\n{content}"
    )
    try:
        response = _model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return content[:200] + "…"


def draft_abstract(text: str) -> str:
    prompt = (
        "Based on the following research paper content, write a concise abstract "
        "(150-250 words) covering: background, objective, methods, results, and conclusion.\n\n"
        f"{text[:3000]}"
    )
    try:
        response = _model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return "Abstract could not be generated."
