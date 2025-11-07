from coding_puzzle_tools import read_input


def main(lines):
    names = lines[0].split(",")
    directions = lines[2].split(",")

    index = 0
    for direction in directions:
        if direction[0] == "R":
            index = min(len(names) - 1, index + int(direction[1]))
        else:
            index = max(0, index - int(direction[1]))

    return names[index]


if __name__ == "__main__":
    print(main(read_input()))
