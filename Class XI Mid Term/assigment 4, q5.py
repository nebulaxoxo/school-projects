''' part 1'''
count = 0
while count <4:
    print('*'*10, end = '\n')
    count +=1

'''part 2'''
for i in range(1, 6):
    print('*'*i, end = '\n')

'''part 3'''
i=0
while(i<=5):
  print(" " * (5 - i) +"*" * i)
  i+=1

'''part 4'''
k = 0

for i in range(1, 6):
    for space in range(1, (5-i)+1):
        print(end="  ")
   
    while k !=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()