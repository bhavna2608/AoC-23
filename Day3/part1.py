def check_digits_with_symbols(input_matrix):
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    sum5=0

    for x in range(rows):
        for y in range(cols):
            # Check if the current position contains a digit
            if input_matrix[x][y].isdigit():
                if 0 < x + 1 < rows and 0 <= y - 1 < cols and (input_matrix[x+1][y-1] in "+-=/@%&*$#" or input_matrix[x-1][y-1] in "+-/=@%&*$#" or input_matrix[x][y-1] in "+-/@=%&*$#" or input_matrix[x-1][y] in "+-=/@%&*$#" or input_matrix[x+1][y] in "+-=/@%&*$#") and input_matrix[x][y-1].isdigit() == False and input_matrix[x][y+1].isdigit() == False:
                    num1 = int(input_matrix[x][y])
                    sum5+= num1
                    print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    
                elif x == 139 and (input_matrix[x-1][y-1] in "+-=/@%&*$#" or input_matrix[x][y-1] in "+-/@%=&*$#" or input_matrix[x-1][y] in "+-/@%&=*$#") and input_matrix[x][y-1].isdigit() == False and input_matrix[x][y+1].isdigit() == False:
                    num1 = int(input_matrix[x][y])
                    sum5+= num1
                    print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    
                elif 0 < x + 1 < rows and 0 < y + 1 < cols and (input_matrix[x+1][y+1] in "+-/@%=&*$#" or input_matrix[x-1][y+1] in "+-/=@%&*$#" or input_matrix[x][y+1] in "+-/@%=&*$#") and input_matrix[x][y-1].isdigit() == False and input_matrix[x][y+1].isdigit() == False:
                    num1 = int(input_matrix[x][y])
                    sum5 += num1
                    print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    
                elif x == 139 and 0 < y + 1 < cols and (input_matrix[x-1][y+1] in "+=-/@%&*$#" or input_matrix[x][y+1] in "+-/=@%&*$#" or input_matrix[x-1][y] in "+-/@%=&*$#") and input_matrix[x][y-1].isdigit() == False and input_matrix[x][y+1].isdigit() == False:
                    num1 = int(input_matrix[x][y])
                    sum5 += num1
                    print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                  
                elif 0 < x + 1 < rows and 0 <= y - 1 < cols and (input_matrix[x+1][y-1] in "+=-/@%&*$#" or input_matrix[x-1][y-1] in "+-=/@%&*$#" or input_matrix[x][y-1] in "+-/=@%&*$#" or input_matrix[x-1][y] in "+-/@=%&*$#" or input_matrix[x+1][y] in "+-=/@%&*$#") and input_matrix[x][y-1].isdigit() == False :
                    if input_matrix[x][y+1].isdigit() == True and input_matrix[x][y+2].isdigit() == True:
                        num1 = 100*int(input_matrix[x][y]) + 10*int(input_matrix[x][y+1]) + int(input_matrix[x][y+2])
                        sum5 += num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                        y = y + 2
                    elif input_matrix[x][y+1].isdigit() == True and input_matrix[x][y+2].isdigit() == False:
                        num1 = 10*int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                        sum5 += num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                        y = y + 1
                    
                elif x == 139 and (input_matrix[x-1][y-1] in "+-/=@%&*$#" or input_matrix[x][y-1] in "+=-/@%&*$#" or input_matrix[x-1][y] in "+-=/@%&*$#") and input_matrix[x][y-1].isdigit() == False :
                    if input_matrix[x][y+1].isdigit() == True and input_matrix[x][y+2].isdigit() == True:
                        num1 = 100*int(input_matrix[x][y]) + 10*int(input_matrix[x][y+1]) + int(input_matrix[x][y+2])
                        sum5+= num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                        y = y + 2
                    elif input_matrix[x][y+1].isdigit() == True and input_matrix[x][y+2].isdigit() == False:
                        num1 = 10*int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                        sum5+= num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                        y = y + 1
                    
                elif 0 < x + 1 < rows and 0 < y + 1 < cols and (input_matrix[x+1][y+1] in "+-=/@%&*$#" or input_matrix[x-1][y+1] in "+-/@=%&*$#" or input_matrix[x][y+1] in "=+-/@%&*$#" or input_matrix[x+1][y] in "+-=/@%&*$#" or input_matrix[x-1][y] in "+-=/@%&*$#") and input_matrix[x][y+1].isdigit() == False :
                    if input_matrix[x][y-1].isdigit() == True and input_matrix[x][y-2].isdigit() == True:
                        num1 = 100*int(input_matrix[x][y-2]) + 10*int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                        sum5+= num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    elif input_matrix[x][y-1].isdigit() == True and input_matrix[x][y-2].isdigit() == False:
                        num1 = 10*int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                        sum5+= num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    
                elif x == 139 and 0 < y + 1 < cols and (input_matrix[x-1][y+1] in "+-/=@%&*$#" or input_matrix[x][y+1] in "+-/=@%&*$#" or input_matrix[x-1][y] in "+-/=@%&*$#") and input_matrix[x][y+1].isdigit() == False :
                    if input_matrix[x][y-1].isdigit() == True and input_matrix[x][y-2].isdigit() == True:
                        num1 = 100*int(input_matrix[x][y-2]) + 10*int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                        sum5+= num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    elif input_matrix[x][y-1].isdigit() == True and input_matrix[x][y-2].isdigit() == False:
                        num1 = 10*int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                        sum5+= num1
                        print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    
                elif 0 < x + 1 < rows and 0 < y + 1 < cols and input_matrix[x+1][y] in "+-/=@%&*$#" and input_matrix[x][y-1].isdigit() == True and input_matrix[x][y+1].isdigit() == True:
                    num1 = 100*int(input_matrix[x][y-1]) + 10*int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                    sum5+= num1
                    print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    y = y + 1
                    
                elif 0 < x < rows and 0 < y + 1 < cols and input_matrix[x-1][y] in "+-/=@%&*$#" and input_matrix[x][y-1].isdigit() == True and input_matrix[x][y+1].isdigit() == True:
                    num1 = 100*int(input_matrix[x][y-1]) + 10*int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                    sum5 += num1
                    print(f"Digit {input_matrix[x][y]} at position ({x}, {y}) has a symbol at position ({num1})")
                    y = y + 1
         
    print(sum5)

# Example usage with a file
def read_input_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        input_matrix = [list(line.strip()) for line in file.readlines()]
    return input_matrix

# Example file path
file_path = r"input.txt"

# Read input matrix from the file
input_matrix = read_input_matrix_from_file(file_path)

# Check digits with symbols in the matrix
check_digits_with_symbols(input_matrix)
