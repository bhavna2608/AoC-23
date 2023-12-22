import numpy as np

def check_hor(arr, i, k, c):
    if i > 0 and k+1 < len(arr):
        for j in range(len(arr[i])):
            count = 0
            if arr[i-1][j] == arr[k+1][j]:
                count = 1
            else:
                c += 1
                count = 1
                if c > 2:
                    return c
    else:
        return c
    if count == 1:
        i = i-1
        k = k+1
        return check_hor(arr, i, k, c)
        
def check_ver(arr, j, k, c):
    if j > 0 and k+1 < len(arr[0]):
        for i in range(len(arr)):
            count = 0
            if arr[i][j-1] == arr[i][k+1]:
                count = 1
            else:
                c += 1
                count = 1
                if c == 2:
                    return c
    else:
        return c
    if count == 1:
        j = j-1
        k = k+1
        return check_ver(arr, j, k, c)

def find_plane_of_reflection(pattern):
    
#     Check for horizontal symmetry
    for i in range(len(arr)-1):
        count = 0
        c = 0
        for j in range(len(arr[i])):
            if arr[i][j] == arr[i+1][j]:
                count = True
            else:
                c += 1
                if c == 2:
                    count = False
                    break
        if count == True:
            tingu = check_hor(arr, i, i+1, c)
            if tingu == 1:
                return 100*(i+1)

    # Check for vertical symmetry
    for j in range(len(arr[0])-1):
        count = 0
        c = 0
        for i in range(len(arr)):
            if arr[i][j] == arr[i][j+1]:
                count = True
            else:
                c += 1
                if c == 2:
                    count = False
                    break
        if count == True:
            tingue = check_ver(arr, j, j+1, c)
            if tingue == 1:
                return j+1
            
with open(r"input.txt", 'r') as file:
    patterns = re.split(r'\n\n+', file.read().strip())

sum13 = 0

for idx, pattern in enumerate(patterns, start=1):
#     print(pattern)

    rows = pattern.strip().split('\n')
    grid = [list(row) for row in rows]

    arr = np.array(grid)

    result = find_plane_of_reflection(pattern)
    sum13 += result
#     print("\n" + "="*40 + "\n")
print(sum13)
