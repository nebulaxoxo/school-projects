#Armstrong number has the sum of the cube of its 
#individual digits equal to the number itself
num = str(input("Enter a number: "))
sum = 0
digit = [int(i) for i in str(num)]
cube = [n**3 for n in digit]

for j in cube:
    sum = sum + j
    
if sum == int(num):
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")

