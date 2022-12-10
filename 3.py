from in3 import *

inarr = text.splitlines()
duplicates = []
def priorityParser(ch):
    value = ord(ch)
    if value > 96:
        return value - 96
    else:
        return value - 38

# Part 1
for line in inarr:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    overlap = ''.join(set(first).intersection(second))
    duplicates.append(overlap)

priorities = map(priorityParser, duplicates)

answer1 = sum(priorities)

# Part 2
duplicates = []

for i in range(0, len(inarr), 3):
    group = [inarr[i], inarr[i + 1], inarr[i + 2]]
    overlap = ''.join(set.intersection(*map(set, group)))
    duplicates.append(overlap)

priorities = map(priorityParser, duplicates)

answer2 = sum(priorities)
print(f'First: {answer1} Second: {answer2}')