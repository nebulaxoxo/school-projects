#Write a program to input n numbers from the user, store them in a tuple, find the maximum and minimum number in the tuple (without using min() and max())
#display them on the monitor, also sort the elements of the tuple in ascending order and display the sorted values.
n = int(input("How many numbers would you like to enter: "))
a = []
for i in range(n):
    x = int(input("Enter a number: "))
    a.append(x)
a = tuple(a)

maxi = 0
for k in a:
    if k>maxi:
        maxi = k
print("Maximum value: ", maxi)

mini = a[0]
for p in a:
    if p<mini:
        mini = p
print("Minimum value: ", mini)
output = tuple(sorted(a))
print("Tuple in ascending order: \n", output)