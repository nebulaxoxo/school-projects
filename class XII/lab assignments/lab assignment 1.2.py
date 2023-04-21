def case_checker(x):
    up = 0
    low = 0
    if type(x) != str:
        print('Invalid input')
    else:
        for i in x: 
            if i.isupper() == True:
                up += 1
            if i.islower() == True:
                low += 1
        print("Upper case letters: ", up, "\nLower case letters: ", low)

'''case_checker(1)
case_checker('nAnDitA')'''
y = input("Enter string: ")
case_checker(y)