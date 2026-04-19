<<<<<<< HEAD
from typing import List
import re
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel("gemini-1.5-flash")


def _split_sections(text: str) -> List[tuple]:
=======
from typing import List, Tuple
import re
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL

_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def _split_sections(text: str) -> List[Tuple[str, str]]:
>>>>>>> ai-service-fix
    """Split text into (title, content) pairs."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    sections = []
    current_title = "Document"
<<<<<<< HEAD
    current_content: list = []
=======
    current_content: List[str] = []
>>>>>>> ai-service-fix

    heading_re = re.compile(
        r"^(abstract|introduction|related work|methodology|results|discussion|conclusion|\d+\.)",
        re.IGNORECASE,
    )

    for para in paragraphs:
        first_line = para.split("\n")[0].strip()
        if heading_re.match(first_line) and len(first_line) < 80:
            if current_content:
<<<<<<< HEAD
                sections.append((current_title, "\n".join(current_content)))
            current_title = first_line
            current_content = [para[len(first_line):].strip()]
=======
                sections.append((current_title, "\n".join(current_content).strip()))
            current_title = first_line
            remaining = para[len(first_line):].strip()
            current_content = [remaining] if remaining else []
>>>>>>> ai-service-fix
        else:
            current_content.append(para)

    if current_content:
<<<<<<< HEAD
        sections.append((current_title, "\n".join(current_content)))
=======
        sections.append((current_title, "\n".join(current_content).strip()))
>>>>>>> ai-service-fix

    return sections or [("Document", text)]


<<<<<<< HEAD
=======
def _gen(prompt: str) -> str:
    if _client is None:
        return ""
    try:
        resp = _client.models.generate_content(
            model=GEMINI_MODEL or "gemini-1.5-flash",
            contents=prompt,
        )
        return (resp.text or "").strip()
    except Exception:
        return ""


>>>>>>> ai-service-fix
def summarize_section(title: str, content: str) -> str:
    prompt = (
        f"Summarize the following '{title}' section of a research paper in 2-3 concise sentences:\n\n{content}"
    )
<<<<<<< HEAD
    try:
        response = _model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return content[:200] + "…"
=======
    out = _gen(prompt)
    return out if out else (content[:200] + "…")
>>>>>>> ai-service-fix


def draft_abstract(text: str) -> str:
    prompt = (
        "Based on the following research paper content, write a concise abstract "
        "(150-250 words) covering: background, objective, methods, results, and conclusion.\n\n"
        f"{text[:3000]}"
    )
<<<<<<< HEAD
    try:
        response = _model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return "Abstract could not be generated."
=======
    out = _gen(prompt)
    return out if out else "Abstract could not be generated."
>>>>>>> ai-service-fix
