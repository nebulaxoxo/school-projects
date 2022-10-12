from timeit import repeat


Pay = []
count = 0
n = int(input("How many employees? "))

if n>= 10:
    for count in range (n):
        x = int(input("Enter value of Pay: "))
        Pay.append(x)
else:
    print("Minimum value of 10 is required.")
    repeat
for i in Pay:
    index = Pay.index(i)
    if i < 100000:
        new = (1/4)*i
        out = new + i
        Pay[index] = out
    if 100000<=i<200000:
        new = (1/5)*i
        out = new + i
        Pay[index] = out
    if i>= 200000:
        new = (3/20)*i
        out = new + i
        Pay[index] = out

print(Pay)