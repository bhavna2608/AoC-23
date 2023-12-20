def find_minimum_counts(record):
    min_red = float(-1)
    min_green = float(-1)
    min_blue = float(-1)

    parts = record.split(':')

    if len(parts) < 2:
        return min_red, min_green, min_blue

    cubes_part = parts[1].strip()

    subsets = [subset.split() for subset in cubes_part.split(';')]

    for subset in subsets:
        for count, color in zip(subset[0::2], subset[1::2]):
            try:
                count = int(count)
            except ValueError:
                continue

            if color == 'red' or color == 'red,':
                min_red = max(min_red, count)
            elif color == 'green' or color == 'green,':
                min_green = max(min_green, count)
            elif color == 'blue' or color == 'blue,':
                min_blue = max(min_blue, count)

    return min_red*min_green*min_blue

def read_records_from_file(file_path):
    with open(file_path, 'r') as file:
        records = file.readlines()
    return records

# Example usage with a file
sum4 = 0
file_path = r"input.txt"
records = read_records_from_file(file_path)

for record in records:
    power = find_minimum_counts(record)
    sum4 += power
    
print(sum4)
