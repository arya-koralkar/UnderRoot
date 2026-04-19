<<<<<<< HEAD
from typing import List
=======
from typing import List, Dict, Any, Tuple
>>>>>>> ai-service-fix
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import SBERT_MODEL

_model = SentenceTransformer(SBERT_MODEL)


<<<<<<< HEAD
def build_index(corpus: List[str]) -> faiss.IndexFlatIP:
    """Build a FAISS IndexFlatIP from a list of corpus sentences."""
=======
def build_semantic_runtime(corpus: List[str]) -> Tuple[faiss.IndexFlatIP, List[str]]:
    """Build FAISS index once for a corpus and return reusable runtime."""
>>>>>>> ai-service-fix
    embeddings = _model.encode(corpus, normalize_embeddings=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype(np.float32))
<<<<<<< HEAD
    return index


def check_semantic(sentences: List[str], corpus: List[str]) -> List[float]:
    """Layer 2: paraphrase-MiniLM-L12-v2 + FAISS IndexFlatIP similarity."""
    if not corpus or not sentences:
        return [0.0] * len(sentences)

    index = build_index(corpus)
    query_embeddings = _model.encode(sentences, normalize_embeddings=True)
    scores_matrix, _ = index.search(query_embeddings.astype(np.float32), k=1)
    return [float(s[0]) for s in scores_matrix]
=======
    return index, corpus


def check_semantic_with_runtime(
    sentences: List[str],
    runtime: Tuple[faiss.IndexFlatIP, List[str]],
) -> List[Dict[str, Any]]:
    """Semantic check using prebuilt FAISS runtime."""
    if not sentences:
        return []

    index, corpus = runtime
    if not corpus:
        return [{"score": 0.0, "source_index": -1, "source_text": ""} for _ in sentences]

    query_embeddings = _model.encode(sentences, normalize_embeddings=True)
    scores_matrix, idx_matrix = index.search(query_embeddings.astype(np.float32), k=1)

    out: List[Dict[str, Any]] = []
    for i in range(len(sentences)):
        best_score = float(scores_matrix[i][0]) if len(scores_matrix[i]) else 0.0
        best_idx = int(idx_matrix[i][0]) if len(idx_matrix[i]) else -1
        best_text = corpus[best_idx] if 0 <= best_idx < len(corpus) else ""
        out.append({
            "score": best_score,
            "source_index": best_idx,
            "source_text": best_text,
        })
    return out


# Backward-compatible helper (optional)
def check_semantic(sentences: List[str], corpus: List[str]) -> List[Dict[str, Any]]:
    if not corpus:
        return [{"score": 0.0, "source_index": -1, "source_text": ""} for _ in sentences]
    runtime = build_semantic_runtime(corpus)
    return check_semantic_with_runtime(sentences, runtime)
>>>>>>> ai-service-fix
