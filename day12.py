def parse(string):
    return (string[0], int(string[1:]))

def rotate(ship, degrees):
    x, y, rot = ship
    new_rot = (rot + degrees) % 360
    return (x, y, new_rot)

def wp_rotate(ship, degrees):
    def rotate_wp_once(ship):
        x, y, wx, wy = ship
        return (x, y, -wy, wx)

    new_ship = ship
    if degrees < 0:
        degrees += 360
    rotations = degrees // 90
    while rotations > 0:
        new_ship = rotate_wp_once(new_ship)
        rotations -= 1

    return new_ship

def move(ship, vector):
    x, y, rot = ship
    vx, vy = vector
    return (x + vx, y + vy, rot)

def wp_move_wp(ship, vector):
    x, y, wx, wy = ship
    vx, vy = vector
    return (x, y, wx + vx, wy + vy)

def wp_move_ship(ship, vector):
    x, y, wx, wy = ship
    vx, vy = vector
    return (x + vx, y + vy, wx, wy)

def move_towards_wp(ship, moves):
    _, _, wx, wy = ship
    new_ship = ship
    while moves > 0:
        new_ship = wp_move_ship(new_ship, (wx, wy))
        moves -= 1

    return new_ship

def facing_dir(ship):
    _, _, rot = ship
    return ['E', 'N', 'W', 'S'][rot // 90]

def wp_execute(ship, ins, val):
    if ins == 'F':
        return move_towards_wp(ship, val)
    elif ins == 'N':
        return wp_move_wp(ship, (0, val))
    elif ins == 'S':
        return wp_move_wp(ship, (0, -val))
    elif ins == 'E':
        return wp_move_wp(ship, (val, 0))
    elif ins == 'W':
        return wp_move_wp(ship, (-val, 0))
    elif ins == 'L':
        return wp_rotate(ship, val)
    elif ins == 'R':
        return wp_rotate(ship, -val)
    else:
        return ship

def execute(ship, ins, val):
    if ins == 'F':
        ins = facing_dir(ship)
    if ins == 'N':
        return move(ship, (0, val))
    elif ins == 'S':
        return move(ship, (0, -val))
    elif ins == 'E':
        return move(ship, (val, 0))
    elif ins == 'W':
        return move(ship, (-val, 0))
    elif ins == 'L':
        return rotate(ship, val)
    elif ins == 'R':
        return rotate(ship, -val)
    else:
        return ship

def part_one(steps):
    ship = (0, 0, 0)
    for s in steps:
        ins, val = parse(s)
        ship = execute(ship, ins, val)

    x, y, _ = ship
    return abs(x) + abs(y)

def part_two(steps):
    ship = (0, 0, 10, 1)
    for s in steps:
        ins, val = parse(s)
        ship = wp_execute(ship, ins, val)

    x, y, _, _ = ship
    return abs(x) + abs(y)

def main():
    steps = []
    with open("day12_input.txt") as f:
        for line in f:
            steps.append(line.strip())

    answer_one = part_one(steps)
    answer_two = part_two(steps)
    print("Part 1 answer:", answer_one)
    print("Part 2 answer:", answer_two)
    #print("Part 2 test:", part_two(["F10", "N3", "F7", "R90", "F11"]))

main()

