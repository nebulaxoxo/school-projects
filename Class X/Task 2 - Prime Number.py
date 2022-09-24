num = int(input("Enter your number: ")) # User inputs number
if num > 1: # As 1 is neither prime nor composite
    for x in range(2,num): # Setting range of all numbers upto input number
        if num % x == 0: # Checking divisibility
            print(num, " is not a prime number.")
            
            break # End loop upon getting desired output
    else: # In case number is not divisible by any in range
        print(num, " is a prime number!")
else: # Numbers less than 1 are not prime
    print(num, " is not a prime number.")

