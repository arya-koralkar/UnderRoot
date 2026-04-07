from typing import List
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import SBERT_MODEL

_model = SentenceTransformer(SBERT_MODEL)


def build_index(corpus: List[str]) -> faiss.IndexFlatIP:
    """Build a FAISS IndexFlatIP from a list of corpus sentences."""
    embeddings = _model.encode(corpus, normalize_embeddings=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype(np.float32))
    return index


def check_semantic(sentences: List[str], corpus: List[str]) -> List[float]:
    """Layer 2: paraphrase-MiniLM-L12-v2 + FAISS IndexFlatIP similarity."""
    if not corpus or not sentences:
        return [0.0] * len(sentences)

    index = build_index(corpus)
    query_embeddings = _model.encode(sentences, normalize_embeddings=True)
    scores_matrix, _ = index.search(query_embeddings.astype(np.float32), k=1)
    return [float(s[0]) for s in scores_matrix]
