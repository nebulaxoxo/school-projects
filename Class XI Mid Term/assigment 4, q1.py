num1, num2 = 0,1
count = 0
n = int(input("Enter number of desired terms: "))
fibonacci = []

while count <= n:
    fibonacci.append(num1)
    next_n = num1 + num2
    num1 = num2
    num2 = next_n
    count +=1 

print(fibonacci)
    