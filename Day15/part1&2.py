def hashz(i):
    count = 0
    for char in i:
        count = ((count + ord(char)) * 17) % 256
    return count

def hashzu(i):
    count = 0
    for char in i:
        if char in "-=":
            break
        count = ((count + ord(char)) * 17) % 256
    return count

def tuktuk(strings):
    boxes = []
    for i in strings:
        box = hashzu(i)
        if i[len(i)-2] == '=':
            for j in range(len(boxes)):
                if boxes[j][1][:-2] == i[0:len(i)-2]:
                    boxes[j][1] = boxes[j][1][:-1] + i[-1]
                    break
            else:
                boxes.append([box, i])
                    
        else:
            for j in range(len(boxes)):
                if boxes[j][1][:-2] == i[0:len(i)-1]:
                    del boxes[j]
                    break
    return boxes

with open(r"input.txt", "r") as f:
        lines = f.read().strip()
        strings = lines.split(',')

sum15a = 0
for i in strings:
    sum15a += hashz(i)
print("Part 1:", sum15a)

sum15b = 0
## part twoooooooooooooooo
boxes = tuktuk(strings)
for i in range(256):
    count = 0
    for j in range(len(boxes)):
        if boxes[j][0] == i:
            count += 1
            sum15b += (i+1)*count*int(boxes[j][1][-1])
print("Part 2:", sum15b)
