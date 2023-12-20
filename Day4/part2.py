def _parse(data):
    for line in data.splitlines():
        if not line:
            continue
        line = line[line.index(":") + 1 :]
        left, right = line.split("|", maxsplit=1)
        left = set(left.split())
        right = set(right.split())
        yield len(left & right)


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read()


def part2(data):
    cards = list(_parse(data))
    counts = [1 for _ in cards]
    for i, card in enumerate(cards):
        for j in range(card):
            counts[i + j + 1] += counts[i]
    return sum(counts)


if __name__ == "__main__":
    file_path = r"input.txt" # Change this to the path of your input file
    input_data = read_input(file_path)
    
    print(part2(input_data))
