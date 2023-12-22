import math
def ding(line, rowcol):
    tingu = []
    
    if line[0] == 'R':
        tingu.append((rowcol[0], rowcol[1] + int(line[1])))
        return tingu

    elif line[0] == 'L':
        tingu.append((rowcol[0], rowcol[1] - int(line[1])))
        return tingu

    elif line[0] == 'U':
        tingu.append((rowcol[0] - int(line[1]), rowcol[1]))
        return tingu

    elif line[0] == 'D':
        tingu.append((rowcol[0] + int(line[1]), rowcol[1]))
        return tingu

start = [(0, 0)]
perimeter = 0
with open(r"input.txt") as file:
    for row in file:
        line = row.split()
        perimeter += int(line[1])
        start.extend(ding(line, start[-1]))
# print(start)
sorted_start = sorted(start, key=lambda x: (x[0], x[1]))

area1 = 0
for i, (x, y) in enumerate(start):
    x2, y2 = start[(i + 1) % len(start)]
    area1 += y * x2 - y2 * x
print(area1 // 2 + perimeter // 2 + 1)
