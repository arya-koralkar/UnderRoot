import re
from typing import List
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
_model = genai.GenerativeModel("gemini-1.5-flash")


def detect_claims(text: str) -> List[str]:
    """Use Gemini 1.5 Flash to identify citable claims in the text."""
    prompt = (
        "You are a scientific writing assistant. Analyze the following text and identify "
        "sentences that are CITABLE_CLAIM (factual statements that need a citation). "
        "Ignore OPINION and GENERAL statements. "
        "Return only the citable claim sentences, one per line, with no extra text.\n\n"
        f"Text:\n{text}"
    )
    try:
        response = _model.generate_content(prompt)
        claims = [
            line.strip()
            for line in response.text.strip().split("\n")
            if line.strip() and len(line.strip()) > 10
        ]
        return claims
    except Exception:
        # Fallback: split on sentence boundaries
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return [s.strip() for s in sentences if len(s.strip()) > 20]
