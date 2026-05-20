from typing import List, Tuple


def find_min_max(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds the minimum and maximum elements using divide and conquer.
    """
    if not numbers:
        raise ValueError("Array must not be empty")

    return _find_min_max_recursive(numbers, 0, len(numbers) - 1)


def _find_min_max_recursive(numbers: List[float], left: int, right: int) -> Tuple[float, float]:
    """
    Recursive helper for finding minimum and maximum values.
    """
    # Recursive logic will be added in the next step.
    return numbers[left], numbers[right]
