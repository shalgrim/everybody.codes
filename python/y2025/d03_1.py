from coding_puzzle_tools import InputMode, read_input


def main(text):
    numbers = [int(n) for n in text.split(",")]
    return sum(set(numbers))


if __name__ == "__main__":
    print(main(read_input(mode=InputMode.TEXT)))
