from in2 import *

inarr = text.splitlines()

# Part 1
shapescores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}
beatby = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
draws = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

scores = []

for line in inarr:
    score = 0
    moves = line.split()
    score += shapescores[moves[1]]

    if beatby[moves[0]] == moves[1]:
        score += 6
    elif draws[moves[0]] == moves[1]:
        score += 3
    
    scores.append(score)

answer1 = sum(scores)

# Part 2
beats = {
    "A": "C",
    "B": "A",
    "C": "B"
}
beatby = {
    "A": "B",
    "B": "C",
    "C": "A"
}

scores = []
for line in inarr:
    score = 0
    moves = line.split()

    if moves[1] == "Y":
        score += 3 + shapescores[moves[0]]
    elif moves[1] == "X":
        score += shapescores[beats[moves[0]]]
    else:
        score += 6 + shapescores[beatby[moves[0]]]
    
    scores.append(score)

answer2 = sum(scores)
print(f'First: {answer1} Second: {answer2}')