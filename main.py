from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


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


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера.
    """
    jobs = [PrintJob(**job) for job in print_jobs]
    printer_constraints = PrinterConstraints(**constraints)
    sorted_jobs = sorted(jobs, key=lambda job: job.priority)

    return {
        "print_order": [job.id for job in sorted_jobs],
        "total_time": printer_constraints.max_items,
    }


if __name__ == "__main__":
    test_min_max_search()
