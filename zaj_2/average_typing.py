from typing import List


def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


print(average([1, 2, 3, 4, 5, 6]))
