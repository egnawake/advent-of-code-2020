# 7b = t
# 13a - 1 = 7b
# 59c - 4 = 7b
# 31d - 6 = 7b
# 19e - 7 = 7b

# t(b[i]) = t(b[0]) + i
# t(b[i]) % b[i] = 0
# t(b[0]) = ??

def part_one(timestamp, buses):
    working_buses = [b for b in buses if b > 0]
    min_wait_times = [(bus, bus - (timestamp % bus)) for bus in working_buses]
    earliest_bus = min(min_wait_times, key=lambda p: p[1])
    return earliest_bus[0] * earliest_bus[1]


def part_two(buses):
    first = -1
    second = -1
    t = buses[0]
    w = buses[0]
    i = 1
    while True:
        if buses[i] < 0:
            i += 1
            continue
        if first < 0 and (t + i) % buses[i] == 0:
            if i >= len(buses) - 1:
                return t
            first = t
            print(first)
        elif second < 0 and (t + i) % buses[i] == 0:
            second = t
            w = second - first
            print("w:", w)
            i += 1
            first = -1
            second = -1
        t += w


def main():
    timestamp = 0
    buses = []
    with open("day13_input.txt") as f:
        l1 = f.readline().strip()
        timestamp = int(l1)
        l2 = f.readline().strip()
        buses = [int(i) if i != "x" else -1 for i in l2.split(",")]

    print("Part 1 answer:", part_one(timestamp, buses))
    print(part_two(buses))


main()

