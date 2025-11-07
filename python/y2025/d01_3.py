def main(lines):
    names = lines[0].split(",")
    num_names = len(names)
    directions = lines[2].split(",")

    for direction in directions:
        toswitch = int(direction[1:]) % num_names
        if direction[0] == "L":
            toswitch = 0 - toswitch
        names[0], names[toswitch] = names[toswitch], names[0]

    return names[0]


if __name__ == "__main__":
    # TODO: Make read_input take a "part"
    with open("../../data/2025/input01_3.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
