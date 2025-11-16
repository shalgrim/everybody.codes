from coding_puzzle_tools import InputMode, read_input
from y2025.d02_1 import add, divide, multiply, parse_from_input


def should_engrave(x, y):
    result = 0, 0
    for _ in range(100):
        result = multiply(result, result)
        result = divide(result, (100_000, 100_000))
        result = add(result, (x, y))
        if any(d < -1_000_000 or d > 1_000_000 for d in [result[0], result[1]]):
            return False
    return True


def main(text):
    A = parse_from_input(text)
    print(f"{A=}")
    answer = 0

    for x in range(A[0], A[0] + 1001, 10):
        for y in range(A[1], A[1] + 1001, 10):
            if should_engrave(x, y):
                answer += 1

    return answer


if __name__ == "__main__":
    print(main(read_input(mode=InputMode.TEXT)))
