import re

def find_first_last_single_digit(input_string):
    # Find all single-digit numbers in the string
    single_digit_numbers = re.findall(r'\d', input_string)

    if single_digit_numbers:
        # Convert the single-digit numbers to integers
        single_digit_numbers = list(map(int, single_digit_numbers))

        # Find the first and last single-digit numbers
        first_single_digit = single_digit_numbers[0]
        last_single_digit = single_digit_numbers[-1]

        return first_single_digit, last_single_digit
    else:
        # No single-digit numbers found in the string
        return None, None

# Read input strings from a file
sum1 = 0
file_path = r"input.txt"
with open(file_path, 'r') as file:
    input_strings = file.readlines()

# Process each input string
for input_str in input_strings:
    first, last = find_first_last_single_digit(input_str)
    sum1 += (10*first) + last
    
print(sum1)
