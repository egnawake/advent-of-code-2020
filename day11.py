def is_position_valid(seat_map, position):
    x, y = position
    return 0 <= y < len(seat_map) and 0 <= x < len(seat_map[0])


def count_visible_occupied_seats(seat_map, position):
    x, y = position
    count = 0

    directions = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]
    for d in directions:
        n_x, n_y = x, y
        while True:
            dx, dy = d
            n_x += dx
            n_y += dy
            if not is_position_valid(seat_map, (n_x, n_y)):
                break
            if seat_map[n_y][n_x] == 'L':
                break
            if seat_map[n_y][n_x] == '#':
                count += 1
                break

    return count


def count_adj_occupied_seats(seat_map, position):
    x, y = position
    adj_seats_positions = [
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1)
    ]

    count = 0
    for pos in adj_seats_positions:
        a_x, a_y = pos
        tile = ''
        if is_position_valid(seat_map, pos):
            tile = seat_map[a_y][a_x]
            if tile == '#':
                count += 1

    return count

            
def step_tile(seat_map, count_occ_seats_strategy, max_occ_seats, position):
    x, y = position
    tile = ''

    if is_position_valid(seat_map, position):
        tile = seat_map[y][x]
        if tile == 'L' and count_occ_seats_strategy(seat_map, position) == 0:
            return '#'
        elif tile == '#' and count_occ_seats_strategy(seat_map, position) >= max_occ_seats:
            return 'L'
        else:
            return tile
    raise IndexError


def step_map(seat_map, count_occ_seats_strategy, max_occ_seats):
    new_map = []
    for y, row in enumerate(seat_map):
        new_row = []
        for x, tile in enumerate(seat_map[y]):
            new_row.append(step_tile(seat_map, count_occ_seats_strategy, max_occ_seats, (x, y)))
        new_map.append(new_row)

    return new_map


def part_one(seat_map):
    count = 0
    cur_map = seat_map
    prev_map = []
    while cur_map != prev_map:
        prev_map = cur_map
        cur_map = step_map(cur_map, count_adj_occupied_seats, 4)

    for row in cur_map:
        for seat in row:
            if seat == '#':
                count += 1

    return count


def part_two(seat_map):
    count = 0
    cur_map = seat_map
    prev_map = []
    while cur_map != prev_map:
        prev_map = cur_map
        cur_map = step_map(cur_map, count_visible_occupied_seats, 5)

    for row in cur_map:
        for seat in row:
            if seat == '#':
                count += 1

    return count


def main():
    seat_map = []

    with open("day11_input.txt") as f:
        for line in f:
            map_row = list(line.strip())
            seat_map.append(map_row)

    print("Part 1 answer:", part_one(seat_map))
    print("Part 2 answer:", part_two(seat_map))


main()

