def parse_ins(string):
    ins = string.split(" ")
    op = ins[0]
    arg = int(ins[1])
    return (op, arg)

def part_one(program):
    pointer = 0
    acc = 0
    ins_ran = []

    while pointer not in ins_ran:
        op, arg = parse_ins(program[pointer])
        ins_ran.append(pointer)
        if op == "acc":
            acc += arg
            pointer += 1
        elif op == "jmp":
            pointer += arg
        else:
            pointer += 1

    return acc

def run_prog(program):
    pointer = 0
    acc = 0
    ins_count = 0
    prog_size = len(program)

    while ins_count < prog_size:
        op, arg = parse_ins(program[pointer])
        ins_count += 1
        if op == "acc":
            acc += arg
            pointer += 1
        elif op == "jmp":
            pointer += arg
        else:
            pointer += 1
        if pointer >= prog_size:
            return acc

    raise Exception

def part_two(program):
    pointer = 0
    acc = 0
    ins_ran = []
    prog_len = len(program)

    for i in range(0, prog_len):
        op, arg = parse_ins(program[i])
        should_change = op == "jmp" or op == "nop"
        if should_change:
            new_ins = ""
            if op == "jmp":
                new_ins += "nop "
            elif op == "nop":
                new_ins += "jmp "
            if arg >= 0:
                new_ins += "+" + str(arg)
            else:
                new_ins += str(arg)
            new_program = program[:i] + [new_ins] + program[i + 1:]
            result = 0
            try:
                result = run_prog(new_program)
            except Exception:
                print("Infinite loop!")
            else:
                return result


def main():
    program = []
    with open("day8_input.txt") as f:
        for line in f:
            program.append(line.strip())
    answer_one = part_one(program)
    answer_two = part_two(program)
    print("Part 1 answer:", answer_one)
    print("Part 2 answer:", answer_two)

main()

