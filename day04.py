import re

def parseFields(line):
    records = line.strip("\n").split(" ")
    fields = [r.split(":") for r in records]
    return dict(fields)

def validateBirthYear(byr):
    if len(byr) != 4 and byr.isdigit():
        return False
    return 1920 <= int(byr) <= 2020

def validateIssueYear(iyr):
    if len(iyr) != 4:
        return False
    return 2010 <= int(iyr) <= 2020

def validateExpirationYear(eyr):
    if len(eyr) != 4:
        return False
    return 2020 <= int(eyr) <= 2030

def validateHeight(hgt):
    if hgt.endswith("cm"):
        return 150 <= int(hgt[:-2]) <= 193
    if hgt.endswith("in"):
        return 59 <= int(hgt[:-2]) <= 76
    return False

def validateHairColor(hcl):
    return re.fullmatch("#[0-9a-f]{6}", hcl)

def validateEyeColor(ecl):
    return ecl in "amb blu brn gry grn hzl oth".split(" ")

def validatePassportId(pid):
    return len(pid) == 9 and pid.isdigit()

def validateCountryId(cid):
    return True

def validatePassport(passport):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "pid", "ecl"]
    hasRequiredFields = True
    for f in requiredFields:
        hasRequiredFields = hasRequiredFields and (f in passport)
    if not hasRequiredFields:
        return False
    return (validateBirthYear(passport["byr"])
        and validateIssueYear(passport["iyr"])
        and validateExpirationYear(passport["eyr"])
        and validateHeight(passport["hgt"])
        and validateHairColor(passport["hcl"])
        and validateEyeColor(passport["ecl"])
        and validatePassportId(passport["pid"]))

def main():
    with open("day4_input.txt") as f:
        count = 0
        passport = {}
        line = "akjshjdk"

        while line != "":
            line = f.readline()
            if line != "\n" and line != "":
                passport.update(parseFields(line))
            else:
                if validatePassport(passport):
                    count += 1
                passport = {}

        print(count)

main()
