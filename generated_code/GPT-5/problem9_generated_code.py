def merge_dicts(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = merged.get(k, 0) + v
    return merged
