def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    return grid

file_path = r"input.txt"
grid = read_input(file_path)

new_grid = []
count = 0
for row in grid:
    count += 1
    if '#' not in row:
        for i in range(2):
            new_grid.append(row)
    else:
        new_grid.append(row)
        
transposed_grid = list(map(list, zip(*new_grid)))
newgrid = []
for c in transposed_grid:
    if '#' not in c:
        for i in range(2):
            newgrid.append(c)
    else:
        newgrid.append(c)

tiku = len(newgrid)
new_grid = list(map(list, zip(*newgrid)))

lst = []
for i in range(len(new_grid)):
    for j in range(tiku):
        if new_grid[i][j] == '#':
            lst.append((i,j))

diff1 = []
diff2 = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        diff1.append(lst[j][0] - lst[i][0])
        diff2.append(abs(lst[j][1] - lst[i][1]))

print(sum(diff1) + sum(diff2))
