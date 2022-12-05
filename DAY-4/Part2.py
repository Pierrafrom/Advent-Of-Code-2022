# Advent of code 2022 DAY-4 by Pierrafrom
import re

def formatLine(ligne):
    dividedLine = ligne.split(",")
    dividedLine[1] = re.sub('[\n]', '', dividedLine[1])
    return dividedLine

f = open("Data.txt")
i = 0
size=0
for line in f:
    pairs = formatLine(line)
    inter1 = pairs[0].split("-")
    inter2 = pairs[1].split("-")
    start1 = int(inter1[0])
    end1 = int(inter1[1])
    start2 = int(inter2[0])
    end2 = int(inter2[1])
    size += 1

    if start1 < start2 and end1 < start2 or start2 < start1 and end2 < start1:
        i += 1

print(size-i)
f.close()
