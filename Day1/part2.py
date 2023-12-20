import re

def find_first_digit(input_string):
    # Find all digits (including spelled-out) in the string
    digits = re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)', input_string, flags=re.IGNORECASE)

    if digits:
        # Convert the digits to integers
        digits = [int(d) if d.isdigit() else {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}[d.lower()] for d in digits]

        # Find the first digit
        first_digit = digits[0]

        return first_digit

def find_last_digit(input_string):
    # Find all digits (including spelled-out) in the string
    digits = re.findall(r'(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)', input_string, flags=re.IGNORECASE)

    if digits:
        # Convert the digits to integers
        digits = [int(d) if d.isdigit() else {"orez": 0, "eno": 1, "owt": 2, "eerht": 3, "ruof": 4, "evif": 5, "xis": 6, "neves": 7, "thgie": 8, "enin": 9}[d.lower()] for d in digits]

        # Find the last digit
        last_digit = digits[0]

        return last_digit
    else:
        return None

sum2 = 0
file_path = r"input.txt"
with open(file_path, 'r') as file:
    input_strings = file.readlines()

# Process each input string
for input_str in input_strings:
    first = find_first_digit(input_str)
    last = find_last_digit(input_str[::-1])
    sum2 += 10*first + last
    
print(sum2)
