import random


def shuffle(solution: list[float, int]) -> list[float, int]:
    result = list(solution)
    random.shuffle(result)
    return result


def is_sorted(solution: list[float, int], ascending: bool) -> bool:
    result = True
    for i in range(len(solution)-1):
        if (ascending):
            if (solution[i] > solution[i+1]):
                result = False
        else:
            if (solution[i] < solution[i+1]):
                result = False
    return result


def bogosort(data: list[float, int], ascending: bool) -> list[float, int]:
    working_data = list(data)
    while (not is_sorted(working_data, ascending)):
        working_data = shuffle(working_data)
    return working_data
