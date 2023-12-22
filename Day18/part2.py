def ding(line, rowcol):
    tingu = []
    
    if line[1] == '0':
        tingu.append((rowcol[0], rowcol[1] + line[0]))
        return tingu

    elif line[1] == '2':
        tingu.append((rowcol[0], rowcol[1] - line[0]))
        return tingu

    elif line[1] == '3':
        tingu.append((rowcol[0] - line[0], rowcol[1]))
        return tingu

    elif line[1] == '1':
        tingu.append((rowcol[0] + line[0], rowcol[1]))
        return tingu
    
line_list = []

with open(r"input.txt") as file:
    for row in file:
        cleaned_row = row.replace("(", "").replace(")", "")
        line_list.append(cleaned_row.split())

lst = []
for i in range(len(line_list)):
    lst.append([line_list[i][2][1:-1], line_list[i][2][-1]])
    
start = [(0, 0)]
perimeter = 0
for i in range(len(lst)):
    lst[i][0] = int(lst[i][0], 16) 
    perimeter += lst[i][0]
    start.extend(ding(lst[i], start[-1]))

area2 = 0
for i, (x, y) in enumerate(start):
    x2, y2 = start[(i + 1) % len(start)]
    area2 += y * x2 - y2 * x
print(area2 // 2 + perimeter // 2 + 1)
