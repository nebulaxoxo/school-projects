def swapper(x,y):
    if type(x) != int or type(y) != int:
        print("Invalid input")
    print("Your first number is: " +  str(x) + "\nYour second number is: " + str(y))
    if x < y:
        print("Swapped!")
        x,y = y, x
        print("Your first number is: " +  str(x) + "\nYour second number is: " + str(y))
    else:
        print("No change")
        print("Your first number is: " +  str(x) + "\nYour second number is: " + str(y))

'''swapper(1,2)
swapper(5,2)'''
n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
swapper(n,m)