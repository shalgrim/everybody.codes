import re
from typing import Tuple

from coding_puzzle_tools import InputMode, read_input


def parse_from_input(text: str) -> Tuple[int, int]:
    pattern = re.compile(r"(?P<x>-?\d+),(?P<y>-?\d+)")
    match = re.search(pattern, text)
    x = int(match.group("x"))
    y = int(match.group("y"))
    return x, y


def add(num1: Tuple[int, int], num2: Tuple[int, int]) -> Tuple[int, int]:
    return num1[0] + num2[0], num1[1] + num2[1]


def multiply(num1: Tuple[int, int], num2: Tuple[int, int]) -> Tuple[int, int]:
    """[X1,Y1] * [X2,Y2] = [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]"""
    x1, y1 = num1
    x2, y2 = num2
    return x1 * x2 - y1 * y2, x1 * y2 + y1 * x2


def divide(num1: Tuple[int, int], num2: Tuple[int, int]) -> Tuple[int, int]:
    """[X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2]"""
    x1, y1 = num1
    x2, y2 = num2

    return x1 // x2, y1 // y2


def perform_operation(result: Tuple[int, int], A: Tuple[int, int]) -> Tuple[int, int]:
    result = multiply(result, result)
    result = divide(result, (10, 10))
    result = add(result, A)
    return result


def main(text):
    A = parse_from_input(text)
    result = 0, 0
    for _ in range(3):
        result = perform_operation(result, A)
    formatted_result = f"[{result[0]},{result[1]}]"
    return formatted_result


if __name__ == "__main__":
    print(main(read_input(mode=InputMode.TEXT)))
