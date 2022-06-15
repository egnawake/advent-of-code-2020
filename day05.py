PLANE_ROWS = 128
PLANE_COLUMNS = 8

def solve_partition(steps, upper, lower, space):
    if len(space) == 1:
        return space[0]
    elif steps[0] == upper:
        return solve_partition(steps[1:], upper, lower, space[len(space) // 2:])
    elif steps[0] == lower:
        return solve_partition(steps[1:], upper, lower, space[:len(space) // 2])

def find_seat_id(boarding_pass):
    row_steps = boarding_pass[:7]
    column_steps = boarding_pass[7:]
    row = solve_partition(row_steps, 'B', 'F', range(PLANE_ROWS))
    column = solve_partition(column_steps, 'R', 'L', range(PLANE_COLUMNS))

    return row * 8 + column;

def part_one():
    max_id = 0
    with open("day5_input.txt") as f:
        for line in f:
            seat_id = find_seat_id(line)
            if seat_id > max_id:
                max_id = seat_id
    return max_id

def part_two():
    seat_ids = []
    with open("day5_input.txt") as f:
        for line in f:
            seat_ids.append(find_seat_id(line))
    seat_ids.sort()
    count = seat_ids[0]
    for i in seat_ids:
        if count != i:
            return count
        count += 1
    return -1

def main():
    print("Part 1 answer:", part_one())
    print("Part 2 answer:", part_two())

main()

