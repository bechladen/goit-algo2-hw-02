from typing import List, Tuple


def find_min_max(numbers: List[float]) -> Tuple[float, float]:
    """
    Знаходить мінімальний та максимальний елементи методом «розділяй і володарюй».
    Повертає кортеж (мінімум, максимум).
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


def test_min_max_search() -> None:
    """
    Перевіряє пошук мінімуму та максимуму на простих прикладах.
    """
    arrays = [
        [5],
        [8, 3],
        [4, 2, 9, 1, 7],
        [10, -3, 25, 0, 14, -8],
    ]

    print("Завдання 1. Пошук мінімального та максимального елементів")
    for numbers in arrays:
        minimum, maximum = find_min_max(numbers)
        print(f"Масив: {numbers}")
        print(f"Мінімум: {minimum}, максимум: {maximum}")


if __name__ == "__main__":
    test_min_max_search()
