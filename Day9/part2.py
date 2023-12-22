def predict_next_value_recursive(history, sum8, count):
#     print(count)
    differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    if count%2 == 0:
        sum8 += differences[0]
    else:
        sum8 -= differences[0]

    if all(diff == 0 for diff in differences):
        return sum8
    else:
        count += 1
        return predict_next_value_recursive(differences, sum8, count)

sequences = []
with open(r"input.txt", "r") as file:
    for line in file:
        sequence = list(map(int, line.split()))
        sequences.append(sequence)
sumfinal = 0

for i, sequence in enumerate(sequences, start=1):
    sum8 = 0
    count = 0
    next_value = sequence[0] - predict_next_value_recursive(sequence, sum8, count)
    sumfinal += next_value
    
print(f"The next value of history_{i} is: {sumfinal}")
