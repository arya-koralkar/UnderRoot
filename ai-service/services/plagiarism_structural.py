from typing import List
from simhash import Simhash


def _hamming_distance(h1: int, h2: int) -> int:
    x = h1 ^ h2
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count


def simhash_fingerprint(text: str) -> int:
    return Simhash(text).value


def structural_similarity(text1: str, text2: str, bits: int = 64) -> float:
    """Layer 3: SimHash + Hamming distance → similarity score."""
    h1 = simhash_fingerprint(text1)
    h2 = simhash_fingerprint(text2)
    distance = _hamming_distance(h1, h2)
    return 1.0 - distance / bits


def check_structural(sentences: List[str], corpus: List[str]) -> List[float]:
    """Compute structural similarity for each sentence against the reference corpus."""
    scores = []
    for sentence in sentences:
        if not corpus:
            scores.append(0.0)
            continue
        max_sim = max(structural_similarity(sentence, ref) for ref in corpus)
        scores.append(max_sim)
    return scores
