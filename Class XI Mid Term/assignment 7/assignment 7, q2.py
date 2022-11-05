#Write a program to input names of n students and store them in a tuple.
#Also, input a name from the user and find if this student is present in the tuple or not
n = int(input("How many students would you like to enter: "))
x = []
for i in range(n):
    a = input("Enter input name: ")
    x.append(a.lower())

x = tuple(x)
name = input("Enter name of student you would like to check the attendance of: ")
if name.lower() not in x:
    print(name.capitalize(), "is absent.")
else:
    print(name, "is present.")
    