a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a+b>=c and a+c>=b and b+c>=a:
    print("Triangle construction is possible.")
else:
    print("Triangle construction is not possible.")