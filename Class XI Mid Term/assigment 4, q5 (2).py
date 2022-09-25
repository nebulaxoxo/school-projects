#part 4
n = 0

for i in range(1, 6):
    for space in range(1, (5-i)+1):
        print(end="  ")   
    while n!=(2*i-1):
        print("* ", end="")
        n += 1  
    n = 0
    print()

#part 5
n = 0

for i in range(1, 6):
    for space in range(1, (5-i)+1):
        print(end="  ")   
    while n!=(2*i-1):
        print(i, end=" ")
        n += 1  
    n = 0
    print()

#part 6
for i in range(1,6):
    for j in range(1, 6-i):
        print(' ', end='')
    for j in range(i,0,-1):
        print(j, end='')
    for j in range(2,i+1):
        print(j, end='')
    print()

#part 7
x = int(input("How many lines of pattern would you like? "))
for i in range(1, x):
    for j in range(65, 65+i):
        a = chr(j)
        print(a, end=" ")
    print()