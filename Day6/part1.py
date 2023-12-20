Time = [48, 98, 90, 83]
Distance = [390, 1103, 1112, 1360]
sum6 = 1

for i in range(len(Time)):
    t = Time[i]
    d = Distance[i]
    count = 0
    for j in range(Time[i]):
        if j*(Time[i]-j) > d:
            count += 1=
    sum6 *= count
print(sum6)
