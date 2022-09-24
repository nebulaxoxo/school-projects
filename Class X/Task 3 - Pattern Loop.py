rows = 5                          # Number of rows in pyramid
space = rows - 1                  # Number of spaces required in each row
for j in range(1, rows + 1) :     # Loop for rows begins
    num = j                       # Variable specification for next loop
    for i in range(1, space + 1) :# Loop to print initial blank spaces 
        print(" ", end=" ")      
    space = space - 1 # Deduct the number of spaces needed in next row
          
    for i in range(1, j + 1) :    # Loop to print numbers in the row begins
        print(num, end=" ")       # Print number series in increasing order
        num = num + 1             # Increment the number by one in every loop
      
    num = num - 2                 # Position back the counter for series 
    for i in range(1, j) :        # Loop to print numbers in the row
        print(num, end=" ")       # Print number series in decreasing order 
        num = num - 1             # Decrement the number by one at each loop
    print("\n")      
    
    
