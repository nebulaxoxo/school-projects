x = input("Enter a string: ")
if len(x) == 2:
    print(x*2)
elif len(x) < 2:
    print("Empty string")
else:
    a = x[:2]
    b = x[-2:]
    print(a+b)
    