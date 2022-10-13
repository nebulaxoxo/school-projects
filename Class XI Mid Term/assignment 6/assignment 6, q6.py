a = []
x = []
num = int(input("How many elements would you like to input? "))
for i in range(num):
    y = int(input("Enter a number: "))
    x.append(y)

for j in x:
    if j not in a:
        a.append(j)
print(x)
print(a)
