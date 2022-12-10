from textwrap import wrap
from in5 import *

inarr = text.splitlines()
startlines = inarr[:8]
moves = inarr[11:]

stacks = []
for line in startlines:
    # Rather than oneliner split amongst these for readability
    split = wrap(line, 4, drop_whitespace=False)
    cleaned = map(lambda s: s.strip("[ ]"), split)
    stacks.append(list(cleaned))

# Same stuff - for readability split from brevity to inefficiency
columns = [[] for i in range(9)]
for stack in reversed(stacks):
    for i in range(0, len(stack)):
        if stack[i] != '':
            columns[i].append(stack[i])

# Part 1
movelist = []
for m in moves:
    # move 6 from 1 to 7 => [6, 1, 7]
    arr = m.split()
    movelist.append(list(map(int, [arr[1], arr[3], arr[5]])))

for move in movelist:
    print("\t{}\n{}\n".format(" ".join(map(str, move)), "\n".join(map(lambda x: str(x[0] + 1) + " " + " ".join(x[1]), enumerate(columns)))))
    for i in range(move[0]):
        fromCol = move[1] - 1
        toCol = move[2] - 1
        crate = columns[fromCol].pop() # Get the latest crate in that column & remove it from that column
        columns[toCol].append(crate) # Set the new crate through move -> col and counter -> cell
    # print("\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A")

answer1 = ""
for col in columns:
    answer1 += col[len(col) - 1]

# Part 2
answer2 = 0

print(f'First: {answer1} Second: {answer2}')