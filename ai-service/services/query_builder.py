from sklearn.feature_extraction.text import TfidfVectorizer

def build_query_from_text(text: str, top_n: int = 10) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    try:
        vec = TfidfVectorizer(stop_words="english", max_features=top_n)
        vec.fit_transform([text[:5000]])
        terms = vec.get_feature_names_out()
        return " ".join(terms[:top_n])
    except Exception:
        return text[:200]