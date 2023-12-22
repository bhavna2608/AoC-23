# works for smaller datasets ans iterations only.
def tuktuk(starting, L, count):
    new_starting = []
    visited = set()
    if count < 500:
        count += 1
        for x, y in starting:
            if L[(x-1)%11][y%11] != '#' and (x-1, y) not in visited:
                new_starting.append((x-1, y))
                visited.add((x-1, y))

            if L[(x+1)%11][y%11] != '#' and (x+1, y) not in visited:
                new_starting.append((x+1, y))
                visited.add((x+1, y))

            if L[x%11][(y-1)%11] != '#' and (x, y-1) not in visited:
                new_starting.append((x, y-1))
                visited.add((x, y-1))

            if L[x%11][(y+1)%11] != '#' and (x, y+1) not in visited:
                new_starting.append((x, y+1))
                visited.add((x, y+1))

        return tuktuk(new_starting, L, count)
    return starting

D = open(r"input.txt").read().strip()
L = D.split('\n')
print(len(L), len(L[1]))
starting = [(i, j) for i in range(len(L)) for j in range(len(L[i])) if L[i][j] == 'S']
visited_set = tuktuk(starting, L, 0)
unique_count = len(visited_set)
print(unique_count)
