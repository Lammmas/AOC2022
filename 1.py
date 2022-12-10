from in1 import *

foods = [[]]
elf = 0

inarr = text.splitlines()

for line in inarr:
    if line == "":
        elf = elf + 1
        foods.append([])
        continue
    foods[elf].append(int(line))
    
calories = []

for food in foods:
    total = 0
    for f in food:
        total = total + f
    calories.append(total)

calories.sort(reverse=True)
answer1 = calories[0]
answer2 = calories[0] + calories[1] + calories[2]
print(f'First: {answer1} Second: {answer2}')