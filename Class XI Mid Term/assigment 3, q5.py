list = []
for i in range(1, 1001):
    for j in range (2, i):
        if i%j == 0:
            break
        else:
            list.append(i)
            break
print("Prime numbers from 1 to 1000 are: /n", list)
