def tuktuk(starting, L, count):
    new_starting = []
    visited = set()
    if count < 64:
        count += 1
        for x, y in starting:
            if x > 0 and L[x-1][y] in '.S' and (x-1, y) not in visited:
                new_starting.append((x-1, y))
                visited.add((x-1, y))

            if x < len(L) - 1 and L[x+1][y] in '.S' and (x+1, y) not in visited:
                new_starting.append((x+1, y))
                visited.add((x+1, y))

            if y > 0 and L[x][y-1] in '.S' and (x, y-1) not in visited:
                new_starting.append((x, y-1))
                visited.add((x, y-1))

            if y < len(L[0]) - 1 and L[x][y+1] in '.S' and (x, y+1) not in visited:
                new_starting.append((x, y+1))
                visited.add((x, y+1))

        return tuktuk(new_starting, L, count)
    return starting

D = open(r"input.txt").read().strip()
L = D.split('\n')
starting = [(i, j) for i in range(len(L)) for j in range(len(L[i])) if L[i][j] == 'S']
visited_set = tuktuk(starting, L, 0)
unique_count = len(visited_set)
print(unique_count)
