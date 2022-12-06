# Advent of code 2022 DAY-5 by Pierrafrom

import re


def formatLine(ligne):
    instructions = ligne.split(' ')
    instructions.pop(0)
    instructions.pop(1)
    instructions.pop(2)
    instructions[2] = re.sub('[\n]', '', instructions[2])
    return instructions


f = open("Data.txt")

stack = [['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T'],
         ['Q', 'R', 'B'],
         ['B', 'Z', 'T', 'Q', 'P', 'M', 'S'],
         ['D', 'V', 'F', 'R', 'Q', 'H'],
         ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P'],
         ['W', 'R', 'T', 'Z'],
         ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J'],
         ['R', 'N', 'F', 'H', 'W'],
         ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']]

for line in f:
    instructions = formatLine(line)
    start = int(instructions[1]) - 1
    destination = int(instructions[2]) - 1
    for i in range(int(instructions[0])):
        size = len(stack[start])
        stack[destination].append(stack[start][size - 1])
        stack[start].pop()

for i in range(len(stack)):
    print(stack[i])

f.close()
