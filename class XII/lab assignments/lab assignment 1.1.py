global alpha
alpha = 'abcdefghijklmnopqrstuvwxyz '
def identifier(nm,ph):
    if type(ph) != int:
        print("Invalid input")

    else:
        out = ''
        for i in str(nm):
            if i.isalpha() == True:
                out = 'Name is valid'
            elif i.isspace() == True:
                out = 'Name is valid'
            else:
                out = 'Name is invalid'
        print(out)

        if len(str(ph)) == 10:
            print("Phone number is valid.")
        else:
            print("Phone number is invalid.")
'''identifier('nandita@', 1234567)
identifier('nandita', 123456790)
identifier(' ', 67577256523753)'''
x = input("Enter your name: ")
y = int(input("Enter your phone number: "))
identifier(x,y)
