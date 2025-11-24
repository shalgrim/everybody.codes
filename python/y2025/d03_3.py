from collections import Counter
from typing import List

from coding_puzzle_tools import InputMode, read_input


def create_packing_set(numbers: List[int]) -> List[int]:
    counter = Counter(numbers)
    answer = []
    for number, count in counter.items():
        for _ in range(count - 1):
            answer.append(number)

    return answer


def main(text: str) -> int:
    numbers = [int(n) for n in text.split(",")]
    answer = 0
    while numbers:
        numbers = create_packing_set(numbers)
        answer += 1

    return answer


if __name__ == "__main__":
    # it says 6 is "too short"
    print(main(read_input(mode=InputMode.TEXT)))
