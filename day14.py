import re


def apply_mask(num, mask):
    result = num
    for i, b in enumerate(mask):
        if b == '1':
            result = result | (2 ** (len(mask) - 1 - i))
        elif b == '0':
            result = result & ~(2 ** (len(mask) - 1 - i))

    return result


def make_instruction(index, args):
    if index == 0:
        return (index, args)
    elif index == 1:
        return (index, (int(args[0]), int(args[1])))
    else:
        return (index, args)


def parse_program(text):
    lines = text.split('\n')
    program = []
    instructions = [
        re.compile(r"mask = (\w{36})"),
        re.compile(r"mem\[(\d+)\] = (\d+)")
    ]
    for l in lines:
        for index, instruction in enumerate(instructions):
            m = instruction.match(l)
            if m:
                program.append(make_instruction(index, m.groups()))

    return program


def run(program):
    registers = {}
    mask = ""
    for ins, args in program:
        if ins == 0:
            mask = args[0]
        elif ins == 1:
            value = apply_mask(args[1], mask)
            registers[args[0]] = value

    return registers


def part_one(inp):
    program = parse_program(inp)
    final_registers = run(program)
    total = 0
    for k in final_registers:
        total = total + final_registers[k]

    return total


def main():
    test_one = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

    inp = ""
    with open("day14_input.txt") as f:
        inp = f.read()

    print("Part 1 answer:", part_one(inp))


main()

