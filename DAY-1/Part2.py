# Advent of Code DAY-1 by Pierrafrom

f = open("Data.txt")

firstElf = 0
secondElf = 0
thirdElf = 0
somme = 0
total = 0

for line in f:
    if line != '\n':
        somme = somme + int(line)
    else:
        if somme > firstElf:
            thirdElf = secondElf
            secondElf = firstElf
            firstElf = somme
        else:
            if somme > secondElf:
                thirdElf = secondElf
                secondElf = somme
            else:
                if somme > thirdElf:
                    thirdElf = somme

        somme = 0
total = firstElf + secondElf + thirdElf
print(total)

f.close()
