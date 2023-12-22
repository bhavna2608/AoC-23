def predict_next_value_recursive(history, sum8):
    differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    sum8 += differences[-1]

    if all(diff == 0 for diff in differences):
        return sum8
    else:
        return predict_next_value_recursive(differences, sum8)

# Read sequences from a file
sequences = []
with open(r"input.txt", "r") as file:
    for line in file:
        sequence = list(map(int, line.split()))
        sequences.append(sequence)
sumfinal = 0

# Process each sequence
for i, sequence in enumerate(sequences, start=1):
    sum8 = 0
    next_value = sequence[-1] + predict_next_value_recursive(sequence, sum8)
    sumfinal += next_value
    
print(f"The next value of history_{i} is: {sumfinal}")
