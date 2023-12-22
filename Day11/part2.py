def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    return grid

file_path = r"input.txt"
grid = read_input(file_path)

list1 = []
count = 0
for row in grid:
    count += 1
    if '#' not in row:
        list1.append(count-1)
    else:
        continue
        
transposed_grid = list(map(list, zip(*grid)))
list2 = []
count = 0
for c in transposed_grid:
    count += 1
    if '#' not in c:
        list2.append(count-1)
    else:
        continue

tiku = len(grid)
new_grid = list(map(list, zip(*newgrid)))

lst = []
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '#':
            lst.append((i,j))

sum11 = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for a in list1:
            if lst[i][0] < a and lst[j][0] >= a:
                sum11 += 999999
        sum11 += lst[j][0] - lst[i][0]
        for a in list2:
            if (lst[i][1] < a and lst[j][1] >= a) or (lst[i][1] > a and lst[j][1] < a):
                sum11 += 999999
        sum11 += abs(lst[j][1] - lst[i][1])

print(sum11)
