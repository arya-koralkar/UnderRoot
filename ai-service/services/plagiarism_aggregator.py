from typing import List, Dict, Any

# Composite weights
W_LEX = 0.3
W_SEM = 0.5
W_STRUCT = 0.2

# Adaptive thresholds per section type
_THRESHOLDS = {
    "abstract": 0.15,
    "introduction": 0.20,
    "related work": 0.35,
    "methodology": 0.20,
    "results": 0.20,
    "discussion": 0.25,
    "conclusion": 0.20,
    "default": 0.25,
}


def _severity(score: float, threshold: float) -> str:
    if score < threshold * 0.5:
        return "low"
    elif score < threshold:
        return "moderate"
    elif score < threshold * 1.5:
        return "high"
    else:
        return "critical"


def aggregate_scores(
    lex_scores: List[float],
    sem_scores: List[float],
    struct_scores: List[float],
) -> List[float]:
    """Combine three layers into composite scores."""
    result = []
    for l, s, st in zip(lex_scores, sem_scores, struct_scores):
        composite = W_LEX * l + W_SEM * s + W_STRUCT * st
        result.append(composite)
    return result


def build_section_result(
    section_title: str,
    sentences: List[str],
    lex_scores: List[float],
    sem_scores: List[float],
    struct_scores: List[float],
) -> Dict[str, Any]:
    composite = aggregate_scores(lex_scores, sem_scores, struct_scores)
    overall = float(sum(composite) / len(composite)) if composite else 0.0

    key = section_title.lower()
    threshold = next(
        (v for k, v in _THRESHOLDS.items() if k in key),
        _THRESHOLDS["default"],
    )
    severity = _severity(overall, threshold)

    matches = []
    for i, (sent, score) in enumerate(zip(sentences, composite)):
        if score > threshold * 0.5:
            matches.append({
                "matched_text": sent[:200],
                "source": "corpus",
                "similarity": round(score, 4),
                "start_index": i,
                "end_index": i + len(sent),
            })

    return {
        "section_title": section_title,
        "overall_score": round(overall, 4),
        "severity": severity,
        "matches": matches,
    }
