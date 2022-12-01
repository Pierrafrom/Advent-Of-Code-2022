# Advent of Code DAY-1 by Pierrafrom

f = open("Data.txt")

maximum = 0
somme = 0

for line in f:
    if line != '\n':
        somme = somme + int(line)
    else:
        if somme > maximum:
            maximum = somme
        somme = 0
print(maximum)

f.close()
