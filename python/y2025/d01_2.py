

def main(lines):
    names = lines[0].split(",")
    num_names = len(names)
    directions = lines[2].split(",")

    index = 0
    for direction in directions:
        distance = int(direction[1:])
        if direction[0] == "R":
            index = (index + distance) % num_names
        else:
            if distance <= index:
                index -= distance
            else:
                # TODO: fix assumption that it would never loop around more than once
                remainder = distance - index
                index = num_names - remainder

    return names[index]


if __name__ == "__main__":
    # TODO: Make read_input take a "part"
    with open("../../data/2025/input01_2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
