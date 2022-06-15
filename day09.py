import itertools

PREAMBLE_SIZE = 25

def is_number_valid(num, prev_nums):
    combos = itertools.combinations(prev_nums, 2)
    for c in combos:
        if sum(c) == num:
            return True
    return False

def part_one(numbers):
    for i in range(PREAMBLE_SIZE, len(numbers)):
        if not is_number_valid(numbers[i], numbers[i - 25:i]):
            return numbers[i]

    raise Exception

def part_two(numbers):
    invalid_num = part_one(numbers)
    for i in range(0, len(numbers)):
        total = numbers[i]
        smallest = numbers[i]
        largest = numbers[i]
        for j in range(i + 1, len(numbers)):
            total += numbers[j]
            smallest = min(smallest, numbers[j])
            largest = max(largest, numbers[j])
            if total == invalid_num:
                return smallest + largest
            elif total > invalid_num:
                break

    raise Exception

def main():
    numbers = []
    with open("day9_input.txt") as f:
        for line in f:
            n = int(line.strip())
            numbers.append(n)

    print("Part 1 answer:", str(part_one(numbers)))
    print("Part 2 answer:", str(part_two(numbers)))

main()

