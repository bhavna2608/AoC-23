def calculate_points(winning_numbers, your_numbers, count):
    points = 0
    matches = set()
    tiktik = set()

    for num in your_numbers:
        if num in winning_numbers and num not in matches:
            matches.add(num)
#             print(matches)
            points = 2 ** (len(matches)-1)
            
#     if points == 0:
    print(count, len(matches), )

    return points

# Read cards data from a file
file_path = r"input.txt"
with open(file_path, 'r') as file:
    cards_data = [line.strip().split('|') for line in file]

total_points = 0
count = 0

for card in cards_data:
    winning_numbers, your_numbers = map(str.split, card)
    winning_numbers = winning_numbers[2:]
    count += 1
#     print(winning_numbers, your_numbers)
    points = calculate_points(winning_numbers, your_numbers, count)
    total_points += points

print(f"The total points for the scratchcards are: {total_points}")
