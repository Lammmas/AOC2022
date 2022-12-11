from in6 import *

# Part 1
idx = 0
for i in range(4, len(text[3:])):
    lastChars = text[i - 4:i]
    if len(set(lastChars)) == len(lastChars):
        idx = i
        break

answer1 = idx

# Part 2
idx = 0
for i in range(14, len(text[13:])):
    lastChars = text[i - 14:i]
    if len(set(lastChars)) == len(lastChars):
        idx = i
        break

answer2 = idx

print(f'First: {answer1} Second: {answer2}')