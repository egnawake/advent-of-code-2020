def part_one():
    count = 0
    with open("day6_input.txt") as f:
        line = "\t"
        all_answers = ""
        while line != "":
            line = f.readline()
            if line != "\n" and line != "":
                all_answers += line.strip()
            else:
                answers = set(all_answers)
                count += len(answers)
                all_answers = ""
    return count


def part_two():
    count = 0
    with open("day6_input.txt") as f:
        line = "\t"
        people_in_group = 0
        answers = {}

        while line != "":
            line = f.readline()
            if line != "\n" and line != "":
                line = line.strip()
                for c in line:
                    if c not in answers:
                        answers[c] = 0
                    answers[c] += 1
                people_in_group += 1
            else:
                for a in answers:
                    if answers[a] == people_in_group:
                        count += 1
                answers = {}
                people_in_group = 0

    return count

                
def main():
    print("Part 1 answer:", part_one())
    print("Part 2 answer:", part_two())

main()

