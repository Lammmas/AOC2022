from in4 import *

inarr = text.splitlines()

parsed = []
for line in inarr:
    sections = line.split(",")
    first = list(map(int, sections[0].split("-")))
    second = list(map(int, sections[1].split("-")))
    parsed.append([first, second])

# Part 1 - full containment
contained = 0
for p in parsed:
    if (p[0][0] <= p[1][0] and p[0][1] >= p[1][1]) or (p[1][0] <= p[0][0] and p[1][1] >= p[0][1]):
        # second is inside the first or first is inside the second
        contained += 1
answer1 = contained

# Part 2 - partial containment
contained = 0
for p in parsed:
    first = p[0]
    second = p[1]

    # this could be done shorter, but readability D:
    if first[0] <= second[0] and first[1] >= second[0]:
        # first ends inside second
        contained += 1
    elif first[0] >= second[0] and first[0] <= second[1]:
        # first starts inside second
        contained += 1
    elif second[0] <= first[0] and second[1] >= first[0]:
        # second ends inside first
        contained += 1
    elif second[0] <= first[1] and second[1] >= first[1]:
        # second starts inside first
        contained += 1

answer2 = contained
print(f'First: {answer1} Second: {answer2}')