from in8 import *

inarr = text.splitlines()

baseGrid = list(map(lambda l: list(map(int, list(l))), inarr))
xposGrid = list(map(list, zip(*baseGrid)))

# Part 1
visibleGrid = {}

row = 0
for line in baseGrid:
    # first horizontals
    col = 0
    visibleGrid[row] = {}

    # First left to right
    largest = 0
    for tree in line:
        visible = False

        if row == 0 or col == 0:
            visible = True
        if tree > largest:
            visible = True
            largest = tree
        
        visibleGrid[row][col] = visible
        col += 1

    # Then right to left
    endIdx = len(line) - 1
    largest = line[endIdx]
    col = endIdx
    for tree in line[::-1]:
        visible = False

        if row == 0 or col == (endIdx):
            visible = True
        elif tree > largest:
            visible = True
            largest = tree
        
        visibleGrid[row][col] = visibleGrid[row][col] or visible
        col -= 1

    row += 1

col = 0
for column in xposGrid:
    # then verticals
    row = 0

    # First top to bottom
    largest = 0
    for tree in column:
        visible = False

        if row == 0 or col == 0:
            visible = True
        if tree > largest:
            visible = True
            largest = tree
        
        visibleGrid[row][col] = visibleGrid[row][col] or visible
        row += 1

    # Then bottom to top
    endIdx = len(column) - 1
    largest = column[endIdx]
    row = endIdx
    for tree in column[::-1]:
        visible = False

        if row == 0 or col == (endIdx):
            visible = True
        elif tree > largest:
            visible = True
            largest = tree
        
        visibleGrid[row][col] = visibleGrid[row][col] or visible
        row -= 1

    col += 1

# Flatten the 2D dict & count True values
answer1 = [j for sub in visibleGrid.values() for j in sub.values()].count(True)

# Part 2
answer2 = 0

print(f'First: {answer1} Second: {answer2}')