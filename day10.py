def can_connect(outp, inp):
    return (inp - outp) <= 3


def build_paths(adapters):
    paths = {}
    for i in range(0, len(adapters)):
        node = adapters[i]
        if node not in paths:
            paths[node] = []
        for j in range(i + 1, len(adapters)):
            target = adapters[j]
            if can_connect(node, target):
                paths[node].append(target)
    return paths


def traverse_path(paths, start):
    memo = {}
    def traverse_path_memoized(start):
        count = 0
        if len(paths[start]) == 0:
            return 1
        for node in paths[start]:
            if node not in memo:
                memo[node] = traverse_path_memoized(node)
            count += memo[node]
        return count

    return traverse_path_memoized(start)
        

def part_one(adapters):
    totals = {}
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff not in totals:
            totals[diff] = 0
        totals[diff] += 1

    return totals[1] * totals[3]


def part_two(adapters):
    paths = build_paths(adapters)
    count = traverse_path(paths, 0)
    return count


def main():
    inp = []
    with open("day10_input.txt") as f:
        for line in f:
            inp.append(line.strip())

    inp = [int(d) for d in inp]
    answer_one = part_one(inp)
    answer_two = part_two(inp)

    print("Part 1 answer:", answer_one)
    print("Part 2 answer:", answer_two)

main()

