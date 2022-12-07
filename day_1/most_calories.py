def parse_input():

    with open("input_day1.txt") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines


def get_elves(lines):

    elves = []
    calories = []
    for line in lines:

        if len(line) == 0:
            elves.append(sum(calories))
            calories = []

        else:
            calories.append(int(line))

    return elves


def main():
    lines = parse_input()
    elves = get_elves(lines)

    max_cals = max(elves)
    top_three_cals = sum(sorted(elves, reverse=True)[:3])

    print(max_cals)
    print(top_three_cals)


if __name__ == "__main__":
    main()
