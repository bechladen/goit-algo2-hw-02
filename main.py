from typing import List, Tuple


def find_min_max(numbers: List[float]) -> Tuple[float, float]:
    """
    Знаходить мінімальний та максимальний елементи методом «розділяй і володарюй».
    """
    if not numbers:
        raise ValueError("Масив не повинен бути порожнім")

    return _find_min_max_recursive(numbers, 0, len(numbers) - 1)


def _find_min_max_recursive(numbers: List[float], left: int, right: int) -> Tuple[float, float]:
    """
    Рекурсивно знаходить мінімум і максимум у частині масиву.
    """
    if left == right:
        return numbers[left], numbers[left]

    if right == left + 1:
        if numbers[left] < numbers[right]:
            return numbers[left], numbers[right]
        return numbers[right], numbers[left]

    middle = (left + right) // 2

    left_min, left_max = _find_min_max_recursive(numbers, left, middle)
    right_min, right_max = _find_min_max_recursive(numbers, middle + 1, right)

    return min(left_min, right_min), max(left_max, right_max)
