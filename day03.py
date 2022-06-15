import math

def findTrees(mapFile, slopeX, slopeY):
    numTrees = 0

    rows = []
    with open("day3_input.txt") as f:
        rows = f.readlines()

    x, y = slopeX, slopeY
    numRows = len(rows)
    rowLen = len(rows[0])

    while y < numRows:
        # each row of the map repeats indefinitely to the right
        # wrap the X coordinate to "move" to the position after the end
        x = x % (rowLen - 1)

        nextChar = rows[y][x]
        if nextChar == '#':
            numTrees += 1

        x += slopeX
        y += slopeY
    return numTrees

def main():
    results = [
        findTrees("day3_input.txt", 1, 1),
        findTrees("day3_input.txt", 3, 1),
        findTrees("day3_input.txt", 5, 1),
        findTrees("day3_input.txt", 7, 1),
        findTrees("day3_input.txt", 1, 2)
    ]
    product = math.prod(results)

    print(product)

main()
