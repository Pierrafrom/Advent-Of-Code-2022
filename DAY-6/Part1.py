# Advent of code 2022 DAY-6 by Pierrafrom

def searchDuplicate(list):
    seen = []
    for i in range(len(list)):
        if list[i] in seen:
            return 1
        else:
            seen.append(list[i])
    return 0


f = open("Data.txt")

string = f.read()
l = [string[0], string[1], string[2], string[3]]
found = searchDuplicate(l)

i = 4
while found == 1:
    l.pop(0)
    l.append(string[i])
    found = searchDuplicate(l)
    i += 1

if found == 0:
    print(l)
    print(i)

f.close()
