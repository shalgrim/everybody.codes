from coding_puzzle_tools import InputMode, read_input


def main(text):
    numbers = [int(n) for n in text.split(",")]
    sorted_unique_numbers = sorted(list(set(numbers)))
    return sum(sorted_unique_numbers[:20])


if __name__ == "__main__":
    print(main(read_input(mode=InputMode.TEXT)))
