from typing import List, Dict, Any

W_LEX = 0.3
W_SEM = 0.5
W_STRUCT = 0.2

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
    return "critical"

def _score(x: Any) -> float:
    return float(x.get("score", 0.0)) if isinstance(x, dict) else float(x)

def aggregate_scores(lex_scores: List[Any], sem_scores: List[Any], struct_scores: List[Any]) -> List[float]:
    out = []
    for l, s, st in zip(lex_scores, sem_scores, struct_scores):
        out.append(W_LEX * _score(l) + W_SEM * _score(s) + W_STRUCT * _score(st))
    return out

def build_section_result(section_title: str, sentences: List[str], lex_scores: List[Any], sem_scores: List[Any], struct_scores: List[Any]) -> Dict[str, Any]:
    composite = aggregate_scores(lex_scores, sem_scores, struct_scores)
    overall = float(sum(composite) / len(composite)) if composite else 0.0

    key = section_title.lower()
    threshold = next((v for k, v in _THRESHOLDS.items() if k in key), _THRESHOLDS["default"])
    severity = _severity(overall, threshold)

    matches = []
    MIN_MATCH_SCORE = 0.35
    for i, (sent, score) in enumerate(zip(sentences, composite)):
        if score > max(threshold * 0.5, MIN_MATCH_SCORE):
            candidates = []
            for layer_name, layer_val in [
                ("lexical", lex_scores[i] if i < len(lex_scores) else {}),
                ("semantic", sem_scores[i] if i < len(sem_scores) else {}),
                ("structural", struct_scores[i] if i < len(struct_scores) else {}),
            ]:
                if isinstance(layer_val, dict):
                    candidates.append({
                        "layer": layer_name,
                        "score": float(layer_val.get("score", 0.0)),
                        "source_index": int(layer_val.get("source_index", -1)),
                        "source_text": layer_val.get("source_text", ""),
                    })

            candidates = [c for c in candidates if c["source_index"] >= 0]
            candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)

            best = candidates[0] if candidates else {"layer": "none", "source_index": -1, "source_text": ""}

            # unique ordered indices
            seen = set()
            idxs = []
            for c in candidates:
                si = c["source_index"]
                if si not in seen:
                    seen.add(si)
                    idxs.append(si)

            matches.append({
                "matched_text": sent[:200],
                "source": "corpus",
                "similarity": round(float(score), 4),
                "start_index": i,
                "end_index": i + len(sent),
                "source_index": best["source_index"],
                "source_text": best["source_text"],
                "source_layer": best["layer"],
                "candidate_source_indices": idxs,  # REQUIRED for top_sources
            })

    return {
        "section_title": section_title,
        "overall_score": round(overall, 4),
        "severity": severity,
        "matches": matches,
    }