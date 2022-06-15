import pprint

def parse_line(line):
    parts = line.strip().split(" contain ")

    color = parts[0].split(" ")
    color = color[0] + color[1]

    contents = parts[1].strip(".")

    if contents.startswith("no"):
        return (color, [])

    contents = contents.split(", ")
    contents = [s.split(" ") for s in contents]
    contents = [(s[1] + s[2], int(s[0])) for s in contents]
    return (color, contents)

def count_bags_inside(rules, bag):
    count = 0
    for rule in rules[bag]:
        rule_bag, rule_amount = rule
        count += rule_amount + rule_amount * count_bags_inside(rules, rule_bag)
    return count

def can_contain(rules, bag, target):
    result = False
    for rule in rules[bag]:
        rule_bag = rule[0]
        if rule_bag == target:
            result = True
        else:
            result = result or can_contain(rules, rule_bag, target)
    return result

def find_containers(rules, bag):
    count = 0
    for b in rules:
        if can_contain(rules, b, bag):
            count += 1
    return count

def main():
    rules = {}
    with open("day7_input.txt") as f:
        for line in f:
            color, contents = parse_line(line)
            rules[color] = contents

    part_one_answer = find_containers(rules, "shinygold")
    part_two_answer = count_bags_inside(rules, "shinygold")

    print("Part 1 answer:", part_one_answer)
    print("Part 2 answer:", part_two_answer)

main()

