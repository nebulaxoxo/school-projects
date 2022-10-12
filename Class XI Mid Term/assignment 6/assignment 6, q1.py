sum = 0
num = []
x = int(input("How many numbers do you want to input? "))
for i in range(x):
    a = int(input("Enter a number: "))
    num.append(a)

for j in num:
    sum = sum + j

print("Sum: ", sum)
