import re

def parseLine(line):
    match = re.search("^(\d+)-(\d+) (\w): (\w+)$", line)
    return match.groups()

def policyOne(minLetters, maxLetters, letter, password):
    charNum = 0
    for c in password:
        if c == letter:
            charNum += 1
    if minLetters <= charNum <= maxLetters:
        return True
    return False

def policyTwo(firstPos, secondPos, letter, password):
    firstPosCheck = password[firstPos - 1] == letter
    secondPosCheck = password[secondPos - 1] == letter
    return firstPosCheck != secondPosCheck

def main():
    lines = []
    with open("day2_input.txt") as f:
        lines = f.readlines()

    policyOneCorrect = 0
    policyTwoCorrect = 0
    for line in lines:
        a, b, letter, password = parseLine(line)
        a = int(a)
        b = int(b)
        if policyOne(a, b, letter, password):
            policyOneCorrect += 1
        if policyTwo(a, b, letter, password):
            policyTwoCorrect += 1
    
    print(f"Policy 1: {policyOneCorrect}")
    print(f"Policy 2: {policyTwoCorrect}")

main()
