num = int(input("Enter a number: "))
list = []
for i in range(1, num+1):
    if num%i == 0:
        if i%2 == 0:
            list.append(i)
        else:
            pass
    else:
        pass

print("Even factors of", num, ": \n", list)

