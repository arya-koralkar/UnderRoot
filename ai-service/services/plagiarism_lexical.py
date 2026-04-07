from typing import List, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_lexical_similarity(source: str, target: str) -> float:
    """Layer 1: TF-IDF with char_wb n-grams (3,5) + cosine similarity."""
    try:
        vectorizer = TfidfVectorizer(
            analyzer="char_wb",
            ngram_range=(3, 5),
            min_df=1,
        )
        matrix = vectorizer.fit_transform([source, target])
        sim = cosine_similarity(matrix[0:1], matrix[1:2])
        return float(sim[0][0])
    except Exception:
        return 0.0


def check_lexical(sentences: List[str], reference_corpus: List[str]) -> List[float]:
    """Compute lexical similarity for each sentence against the reference corpus."""
    scores = []
    for sentence in sentences:
        if not reference_corpus:
            scores.append(0.0)
            continue
        max_sim = max(
            compute_lexical_similarity(sentence, ref) for ref in reference_corpus
        )
        scores.append(max_sim)
    return scores
