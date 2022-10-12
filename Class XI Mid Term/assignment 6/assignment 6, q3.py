n = int(input("How many numbers would you like to input? "))
num = []
for i in range (n):
    x = int(input("Enter a number: "))
    num.append(x)
pos = []
neg = []
for j in num:
    if j>=0:
        pos.append(j)
    else: 
        neg.append(j)

print("Positive integers:\n", pos, "\nNegative integers: \n", neg)
