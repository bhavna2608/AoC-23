x_lim = 200000000000000
y_lim = 400000000000000

inputi = []
with open(r"input.txt", "r") as file:
    for t in file:
        Line = t.strip()
        inputi.append(Line)

posi = []
velo = []

for a in range(len(inputi)):
    posi.append(inputi[a].split('@')[0])
    velo.append(inputi[a].split('@')[1])

for i in range(len(posi)):
    posi[i] = [int(coord) for coord in posi[i].split(',')]
    velo[i] = [int(speed) for speed in velo[i].split(',')]

count = 0

for i in range(len(posi)-1):
    for j in range(i + 1, len(posi)):
        x1, y1, z1 = posi[i]
        x3, y3, z3 = posi[j]
        vx1, vy1, vz1 = velo[i]
        vx2, vy2, vz2 = velo[j]

        den = (-vx1*(-vy2)) - (-vy1*(-vx2))

        if den != 0:
            num1 = (x1*(y1+vy1)) - (y1*(x1+vx1))
            num2 = (x3*(y3+vy2)) - (y3*(x3+vx2))

            x = ((num1*(-vx2)) - (num2*(-vx1)))/den
            y = ((num1*(-vy2)) - (num2*(-vy1)))/den
            
            if (vx1 >= 0 and x < x1) or (vx1 <= 0 and x > x1) or (vx2 >= 0 and x < x3) or (vx2 <= 0 and x > x3):
                continue
            else:
                if x_lim <= x <= y_lim and x_lim <= y <= y_lim:
                    count += 1
                
        else:
            continue

print(count)
