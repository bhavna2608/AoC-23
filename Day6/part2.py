Time = [48989083]
Distance = [390110311121360]
sum6 = 1

for i in range(len(Time)):
    t = Time[i]
    d = Distance[i]
    count = 0
    for j in range(Time[i]):
        if j*(Time[i]-j) > d:
            count += 1
    sum6 *= count
print(sum6)
