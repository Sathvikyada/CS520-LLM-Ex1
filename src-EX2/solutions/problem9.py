from typing import Dict, Any


def merge_dicts(d1: Dict[Any, int], d2: Dict[Any, int]) -> Dict[Any, int]:
    """Merge two dictionaries summing the values for matching keys."""
    merged = d1.copy()
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

