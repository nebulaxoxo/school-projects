while 1+1 == 2:
    a = str(input("Press f to convert celsius to fahrenheit. Press c to convert fahrenheit to celsius. "))
    if a.lower() == 'f':
        num = int(input("Enter temperature in celsius (only digits): "))
        output = ((num*9)/5)+32
        print (num,'C in fahrenheit is: ', output, '\n')
        x = input("Would you like to make another conversion? [y/n]: ")
        if x == 'n':
            quit()
        if x == 'y':
            continue
        
    elif a.lower() == 'c':
            num2 = int(input("Enter temperature in fahrenheit (only digits): "))
            output2 = ((num2-32)/9)*5
            print (num2, "F in celsius is: ", output2)
            z = input("Would you like to make another conversion? [y/n]: ")
            if z == 'n':
                quit()
            if z == 'y':
                continue
    else:
        print('Please enter valid input.')
        continue
    
    