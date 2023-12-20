def check_digits_with_symbols(input_matrix):
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    sum6=0

    for x in range(rows):
        for y in range(cols):
            if input_matrix[x][y].isdigit():
                numone, numtwo, numtwo2 = 0, 0, 0

                if 0 < x + 2 < rows and 0 <= y < cols and y + 2 < cols and input_matrix[x+1][y+1] == '*' and not input_matrix[x][y+1].isdigit():
                    if input_matrix[x][y-1].isdigit() and input_matrix[x][y-2].isdigit():
                        numone = 100 * int(input_matrix[x][y-2]) + 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    elif input_matrix[x][y-1].isdigit() and not input_matrix[x][y-2].isdigit():
                        numone = 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    else:
                        numone = int(input_matrix[x][y])

                    if 0 <= x + 2 < rows and 0 <= y + 4 < cols and input_matrix[x+2][y+2].isdigit() and not input_matrix[x+2][y+1].isdigit():
                        if input_matrix[x+2][y+3].isdigit() and input_matrix[x+2][y+4].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y+2]) + 10 * int(input_matrix[x+2][y+3]) + int(input_matrix[x+2][y+4])
                        elif input_matrix[x+2][y+3].isdigit() and not input_matrix[x+2][y+4].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y+2]) + int(input_matrix[x+2][y+3])
                        else:
                            numtwo = int(input_matrix[x+2][y+2])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y+2].isdigit() and input_matrix[x+2][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y+1]) + 10 * int(input_matrix[x+2][y+2]) + int(input_matrix[x+2][y+3])
                        elif input_matrix[x+2][y+2].isdigit() and not input_matrix[x+2][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        else:
                            numtwo = int(input_matrix[x+2][y+1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y-1].isdigit():
                        if input_matrix[x+2][y+1].isdigit() and input_matrix[x+2][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y]) + 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        elif input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                    
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y+2].isdigit():
                        if input_matrix[x+2][y].isdigit() and input_matrix[x+2][y-1].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-1]) + 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        elif input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y-1].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                        if input_matrix[x+2][y-1].isdigit() and input_matrix[x+2][y-2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-2]) + 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        elif input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y].isdigit():
                        if input_matrix[x+1][y-1].isdigit() and input_matrix[x+1][y-2].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-2]) + 10 * int(input_matrix[x+1][y-1]) + int(input_matrix[x+1][y])
                        elif input_matrix[x+1][y-1].isdigit() and not input_matrix[x+1][y-2].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-1]) + int(input_matrix[x+1][y])
                        else:
                            numtwo = int(input_matrix[x+1][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y+2].isdigit():
                        if input_matrix[x+1][y+4].isdigit() and input_matrix[x+1][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y+2]) + 10 * int(input_matrix[x+1][y+3]) + int(input_matrix[x+1][y+4])
                        elif input_matrix[x+1][y+3].isdigit() and not input_matrix[x+1][y+4].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y+2]) + int(input_matrix[x+1][y+3])
                        else:
                            numtwo = int(input_matrix[x+1][y+2])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x][y+2].isdigit():
                        if input_matrix[x][y+4].isdigit() and input_matrix[x][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x][y+2]) + 10 * int(input_matrix[x][y+3]) + int(input_matrix[x][y+4])
                        elif input_matrix[x][y+3].isdigit() and not input_matrix[x][y+4].isdigit():
                            numtwo = 10 * int(input_matrix[x][y+2]) + int(input_matrix[x][y+3])
                        else:
                            numtwo = int(input_matrix[x][y+2])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                
                            
                elif 0 < x + 2 < rows and 0 <= y - 2 < cols and y+4 < cols and input_matrix[x+1][y] == '*' and not input_matrix[x][y+1].isdigit():
                    if input_matrix[x][y-1].isdigit() and input_matrix[x][y-2].isdigit():
                        numone = 100 * int(input_matrix[x][y-2]) + 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    elif input_matrix[x][y-1].isdigit() and not input_matrix[x][y-2].isdigit():
                        numone = 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    else:
                        numone = int(input_matrix[x][y])
                        
                    if 0 <= x + 2 < rows and 0 <= y + 4 < cols and input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y+2].isdigit() and input_matrix[x+2][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y+1]) + 10 * int(input_matrix[x+2][y+2]) + int(input_matrix[x+2][y+3])
                        elif input_matrix[x+2][y+2].isdigit() and not input_matrix[x+2][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        else:
                            numtwo = int(input_matrix[x+2][y+1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                        if input_matrix[x+2][y].isdigit() and input_matrix[x+2][y+1].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-1]) + 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        elif input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y-1].isdigit():
                        if input_matrix[x+2][y+1].isdigit() and input_matrix[x+2][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y]) + 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        elif input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                        if input_matrix[x+2][y-1].isdigit() and input_matrix[x+2][y-2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-2]) + 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        elif input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y-2].isdigit() and input_matrix[x+2][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-3]) + 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        elif input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        else:
                            numtwo = int(input_matrix[x+2][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y-1].isdigit():
                        if input_matrix[x+1][y-2].isdigit() and input_matrix[x+1][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-3]) + 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        elif input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        else:
                            numtwo = int(input_matrix[x+1][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y+1].isdigit():
                        if input_matrix[x+1][y+2].isdigit() and input_matrix[x+1][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y+1]) + 10 * int(input_matrix[x+1][y+2]) + int(input_matrix[x+1][y+3])
                        elif input_matrix[x+1][y+2].isdigit() and not input_matrix[x+1][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        else:
                            numtwo = int(input_matrix[x+1][y+1])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                            
                elif 0 < x + 2 < rows and 0 <= y - 2 < cols and y+4 < cols and input_matrix[x+1][y] == '*' and not input_matrix[x][y-1].isdigit():
                    if input_matrix[x][y+1].isdigit() and input_matrix[x][y+2].isdigit():
                        numone = 100 * int(input_matrix[x][y]) + 10 * int(input_matrix[x][y+1]) + int(input_matrix[x][y+2])
                    elif input_matrix[x][y+1].isdigit() and not input_matrix[x][y+2].isdigit():
                        numone = 10 * int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                    else:
                        numone = int(input_matrix[x][y])
                        
                    if 0 <= x + 2 < rows and 0 <= y + 4 < cols and input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y+2].isdigit() and input_matrix[x+2][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y+1]) + 10 * int(input_matrix[x+2][y+2]) + int(input_matrix[x+2][y+3])
                        elif input_matrix[x+2][y+2].isdigit() and not input_matrix[x+2][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        else:
                            numtwo = int(input_matrix[x+2][y+1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 4 < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y-1].isdigit():
                        if input_matrix[x+2][y+1].isdigit() and input_matrix[x+2][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y]) + 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        elif input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 4 < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                        if input_matrix[x+2][y].isdigit() and input_matrix[x+2][y+1].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-1]) + 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        elif input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y-2].isdigit() and input_matrix[x+2][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-3]) + 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        elif input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                        if input_matrix[x+2][y-2].isdigit() and input_matrix[x+2][y-1].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-2]) + 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        elif input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y-1].isdigit():
                        if input_matrix[x+1][y-2].isdigit() and input_matrix[x+1][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-3]) + 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        elif input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        else:
                            numtwo = int(input_matrix[x+1][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y+1].isdigit():
                        if input_matrix[x+1][y+2].isdigit() and input_matrix[x+1][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y+1]) + 10 * int(input_matrix[x+1][y+2]) + int(input_matrix[x+1][y+3])
                        elif input_matrix[x+1][y+2].isdigit() and not input_matrix[x+1][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        else:
                            numtwo = int(input_matrix[x+1][y+1])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                            
                            
                elif 0 < x < rows and 0 <= y < cols and y+1 < cols and input_matrix[x-1][y+1] == '*' and not input_matrix[x][y+1].isdigit():
                    if input_matrix[x][y-1].isdigit() and input_matrix[x][y-2].isdigit():
                        numone = 100 * int(input_matrix[x][y-2]) + 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    elif input_matrix[x][y-1].isdigit() and not input_matrix[x][y-2].isdigit():
                        numone = 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    else:
                        numone = int(input_matrix[x][y])
                        
                    if input_matrix[x][y+2].isdigit():
                        if input_matrix[x][y+3].isdigit() and input_matrix[x][y+4].isdigit():
                            numtwo = 100 * int(input_matrix[x][y+2]) + 10 * int(input_matrix[x][y+3]) + int(input_matrix[x][y+4])
                        elif input_matrix[x][y+3].isdigit() and not input_matrix[x][y+4].isdigit():
                            numtwo = 10 * int(input_matrix[x][y+2]) + int(input_matrix[x][y+3])
                        else:
                            numtwo = int(input_matrix[x][y+2])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                            
                elif 0 < x < rows and 0 <= y < cols and input_matrix[x][y-1] == '*':
                    if input_matrix[x][y+1].isdigit() and input_matrix[x][y+2].isdigit():
                        numone = 100 * int(input_matrix[x][y]) + 10 * int(input_matrix[x][y+1]) + int(input_matrix[x][y+2])
                    elif input_matrix[x][y+1].isdigit() and not input_matrix[x][y+2].isdigit():
                        numone = 10 * int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                    else:
                        numone = int(input_matrix[x][y])
                        
                    if 0 <= x + 2 < rows and 0 <= y + 4 < cols and input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y-1].isdigit():
                        if input_matrix[x+1][y+1].isdigit() and input_matrix[x+1][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y]) + 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        elif input_matrix[x+1][y+1].isdigit() and not input_matrix[x+1][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        else:
                            numtwo = int(input_matrix[x+1][y+1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y-3].isdigit():
                        if input_matrix[x+1][y].isdigit() and input_matrix[x+1][y+1].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-1]) + 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        elif input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y+1].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-1]) + int(input_matrix[x+1][y])
                        else:
                            numtwo = int(input_matrix[x+1][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y].isdigit():
                        if input_matrix[x+1][y-3].isdigit() and input_matrix[x+1][y-4].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-4]) + 10 * int(input_matrix[x+1][y-3]) + int(input_matrix[x+1][y-2])
                        elif input_matrix[x+1][y-3].isdigit() and not input_matrix[x+1][y-4].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-3]) + int(input_matrix[x+1][y-2])
                        else:
                            numtwo = int(input_matrix[x+1][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y-3].isdigit():
                        if input_matrix[x+1][y].isdigit() and input_matrix[x+1][y+1].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-1]) + 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        elif input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y+1].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-1]) + int(input_matrix[x+1][y])
                        else:
                            numtwo = int(input_matrix[x+1][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y-1].isdigit():
                        if input_matrix[x+1][y+1].isdigit() and input_matrix[x+1][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y]) + 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        elif input_matrix[x+1][y+1].isdigit() and not input_matrix[x+1][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        else:
                            numtwo = int(input_matrix[x+1][y])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+1][y-1].isdigit() and not input_matrix[x+1][y].isdigit():
                        if input_matrix[x+1][y-2].isdigit() and input_matrix[x+1][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-3]) + 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][-1])
                        elif input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        else:
                            numtwo = int(input_matrix[x+1][y-1])
                            
                    elif 0 <= x < rows and 0 < y < cols and input_matrix[x][y-2].isdigit():
                        if input_matrix[x][y-3].isdigit() and input_matrix[x][y-4].isdigit():
                            numtwo = 100 * int(input_matrix[x][y-4]) + 10 * int(input_matrix[x][y-3]) + int(input_matrix[x][y-2])
                        elif input_matrix[x][y-3].isdigit() and not input_matrix[x][y-4].isdigit():
                            numtwo = 10 * int(input_matrix[x][y-3]) + int(input_matrix[x][y-2])
                        else:
                            numtwo = int(input_matrix[x][y-2])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                            
                elif 0 < x < rows and 0 <= y+1 < cols and input_matrix[x][y+1] == '*':
                    if input_matrix[x][y-1].isdigit() and input_matrix[x][y-2].isdigit():
                        numone = 100 * int(input_matrix[x][y-2]) + 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    elif input_matrix[x][y-1].isdigit() and not input_matrix[x][y-2].isdigit():
                        numone = 10 * int(input_matrix[x][y-1]) + int(input_matrix[x][y])
                    else:
                        numone = int(input_matrix[x][y])
                        
                    if 0 < x < rows and 0 < y + 1 < cols and input_matrix[x+1][y+2].isdigit() and not input_matrix[x+1][y+1].isdigit():
                        if input_matrix[x+1][y+3].isdigit() and input_matrix[x+1][y+4].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y+2]) + 10 * int(input_matrix[x+1][y+3]) + int(input_matrix[x+1][y+4])
                        elif input_matrix[x+1][y+3].isdigit() and not input_matrix[x+1][y+4].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y+2]) + int(input_matrix[x+1][y+3])
                        else:
                            numtwo = int(input_matrix[x+2][y+2])
                            
                    elif 0 <= x + 1 < rows and 0 <= y + 1 < cols and input_matrix[x+1][y+1].isdigit() and not input_matrix[x+1][y].isdigit():
                        if input_matrix[x+1][y+2].isdigit() and input_matrix[x+1][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y+1]) + 10 * int(input_matrix[x+1][y+2]) + int(input_matrix[x+1][y+3])
                        elif input_matrix[x+1][y+2].isdigit() and not input_matrix[x+1][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        else:
                            numtwo = int(input_matrix[x+1][y+1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 2 < cols and input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y-1].isdigit():
                        if input_matrix[x+1][y+1].isdigit() and input_matrix[x+1][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y]) + 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        elif input_matrix[x+1][y+1].isdigit() and not input_matrix[x+1][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        else:
                            numtwo = int(input_matrix[x+1][y])
                    
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y+1].isdigit() and not input_matrix[x+1][y+2].isdigit():
                        if input_matrix[x+1][y].isdigit() and input_matrix[x+1][y-1].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-1]) + 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        elif input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y-1].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+1][y].isdigit() and not input_matrix[x+1][y+1].isdigit():
                        if input_matrix[x+1][y-1].isdigit() and input_matrix[x+1][y-2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-2]) + 10 * int(input_matrix[x+1][y-1]) + int(input_matrix[x+1][y])
                        elif input_matrix[x+1][y-1].isdigit() and not input_matrix[x+1][y-2].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-1]) + int(input_matrix[x+1][y])
                        else:
                            numtwo = int(input_matrix[x+1][y])
                     
 #                 elif 0 < x < rows and 0 <= y+1 < cols and input_matrix[x][y+1] == '*':
#                     if 
                            
#                     if input_matrix[x+1][y] == '*' and input_matrix[x+1][y+1].isdigit():
#                         print("YAYAYA")

                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")

                elif 0 < x+1 < rows and 0 < y < cols and input_matrix[x+1][y-1] == '*' and not input_matrix[x][y-1].isdigit():
                    if input_matrix[x][y+1].isdigit() and input_matrix[x][y+2].isdigit():
                        numone = 100 * int(input_matrix[x][y]) + 10 * int(input_matrix[x][y+1]) + int(input_matrix[x][y+2])
                    elif input_matrix[x][y+1].isdigit() and not input_matrix[x][y+2].isdigit():
                        numone = 10 * int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                    else:
                        numone = int(input_matrix[x][y])
                        
                    if 0 <= x + 2 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y-1].isdigit():
                        if input_matrix[x+2][y+1].isdigit() and input_matrix[x+2][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y]) + 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        elif input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y+1])
                            
                    elif 0 <= x + 1 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                        if input_matrix[x+2][y].isdigit() and input_matrix[x+2][y+1].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-1]) + 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        elif input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-1].isdigit():
                        if input_matrix[x+2][y-3].isdigit() and input_matrix[x+2][y-4].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-4]) + 10 * int(input_matrix[x+2][y-3]) + int(input_matrix[x+2][y-2])
                        elif input_matrix[x+2][y-3].isdigit() and not input_matrix[x+2][y-4].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-3]) + int(input_matrix[x+2][y-2])
                        else:
                            numtwo = int(input_matrix[x+2][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 <= y < cols and input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-3].isdigit():
                        if input_matrix[x+2][y-1].isdigit() and input_matrix[x+2][y].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-2]) + 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        elif input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        else:
                            numtwo = int(input_matrix[x+2][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y-2].isdigit() and input_matrix[x+2][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-3]) + 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        elif input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        else:
                            numtwo = int(input_matrix[x+2][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+1][y].isdigit():
                        if input_matrix[x+1][y+1].isdigit() and input_matrix[x+1][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y]) + 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        elif input_matrix[x+1][y+1].isdigit() and not input_matrix[x+1][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y]) + int(input_matrix[x+1][y+1])
                        else:
                            numtwo = int(input_matrix[x+1][y])
                            
                    elif 0 <= x < rows and 0 < y < cols and input_matrix[x+1][y-2].isdigit():
                        if input_matrix[x+1][y-3].isdigit() and input_matrix[x+1][y-4].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-4]) + 10 * int(input_matrix[x+1][y-3]) + int(input_matrix[x+1][y-2])
                        elif input_matrix[x+1][y-3].isdigit() and not input_matrix[x+1][y-4].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-3]) + int(input_matrix[x+1][y-2])
                        else:
                            numtwo = int(input_matrix[x+1][y-2])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                        
                elif 0 < x+2 < rows and 0 < y < cols and input_matrix[x+1][y] == '*' and input_matrix[x][y-1].isdigit() and input_matrix[x][y+1].isdigit():
                    numone = 100 * int(input_matrix[x][y-1]) + 10 * int(input_matrix[x][y]) + int(input_matrix[x][y+1])
                    
                    if 0 <= x + 2 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y+2].isdigit() and input_matrix[x+2][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y+1]) + 10 * int(input_matrix[x+2][y+2]) + int(input_matrix[x+2][y+3])
                        elif input_matrix[x+2][y+2].isdigit() and not input_matrix[x+2][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        else:
                            numtwo = int(input_matrix[x+2][y+1])
                            
                    elif 0 <= x + 1 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y-2].isdigit():
                        if input_matrix[x+2][y].isdigit() and input_matrix[x+2][y+1].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-1]) + 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        elif input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y+1].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        else:
                            numtwo = int(input_matrix[x+2][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 < y < cols and input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y].isdigit():
                        if input_matrix[x+2][y-2].isdigit() and input_matrix[x+2][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-3]) + 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        elif input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        else:
                            numtwo = int(input_matrix[x+2][y-1])
                            
                    elif 0 <= x + 2 < rows and 0 <= y < cols and input_matrix[x+2][y-2].isdigit() and not input_matrix[x+2][y-3].isdigit():
                        if input_matrix[x+2][y-1].isdigit() and input_matrix[x+2][y].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y-2]) + 10 * int(input_matrix[x+2][y-1]) + int(input_matrix[x+2][y])
                        elif input_matrix[x+2][y-1].isdigit() and not input_matrix[x+2][y].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y-2]) + int(input_matrix[x+2][y-1])
                        else:
                            numtwo = int(input_matrix[x+2][y-2])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 2 < cols and input_matrix[x+2][y].isdigit() and not input_matrix[x+2][y-1].isdigit():
                        if input_matrix[x+2][y+1].isdigit() and input_matrix[x+2][y+2].isdigit():
                            numtwo = 100 * int(input_matrix[x+2][y]) + 10 * int(input_matrix[x+2][y+1]) + int(input_matrix[x+2][y+2])
                        elif input_matrix[x+2][y+1].isdigit() and not input_matrix[x+2][y+2].isdigit():
                            numtwo = 10 * int(input_matrix[x+2][y]) + int(input_matrix[x+2][y+1])
                        else:
                            numtwo = int(input_matrix[x+2][y])
                            
                    elif 0 <= x + 2 < rows and 0 <= y + 3 < cols and input_matrix[x+1][y+1].isdigit():
                        if input_matrix[x+1][y+2].isdigit() and input_matrix[x+1][y+3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y+1]) + 10 * int(input_matrix[x+1][y+2]) + int(input_matrix[x+1][y+3])
                        elif input_matrix[x+1][y+2].isdigit() and not input_matrix[x+1][y+3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y+1]) + int(input_matrix[x+1][y+2])
                        else:
                            numtwo = int(input_matrix[x+1][y+1])
                            
                    elif 0 <= x < rows and 0 < y < cols and input_matrix[x+1][y-1].isdigit():
                        if input_matrix[x+1][y-2].isdigit() and input_matrix[x+1][y-3].isdigit():
                            numtwo = 100 * int(input_matrix[x+1][y-3]) + 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        elif input_matrix[x+1][y-2].isdigit() and not input_matrix[x+1][y-3].isdigit():
                            numtwo = 10 * int(input_matrix[x+1][y-2]) + int(input_matrix[x+1][y-1])
                        else:
                            numtwo = int(input_matrix[x+1][y-1])
                            
                    if numone != 0 and numtwo != 0:
                        sum6 += numone * numtwo
                        print(f"Rows and cols at {x} {y} with {numone} and {numtwo}")
                             
                        
    print(sum6)

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
