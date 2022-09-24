def factorial():
    num = int(input("Enter a number: "))
    one = 1
    for i in range(1, num+1):
        one = one*i
    print(num, "! =", one)

factorial()
