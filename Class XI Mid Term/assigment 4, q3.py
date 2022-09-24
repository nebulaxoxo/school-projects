n = int(input("Enter number of desired terms: "))
list = []

for i in range(1, n+1):
    list.append(1/i)
print("Your series is (in decimal form): ", list)
add = [k for k in list]
print("The summation of your series is: ", sum(add))

