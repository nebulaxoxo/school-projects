#Write a program to read email IDs of n number of students and store them in a tuple.
#Create two new tuples, one to store only the usernames from the email IDs and second to store domain names from the email ids. 
# Print all three tuples at the end of the program.
x = []
names = []
domains = []
n = int(input("Enter number of students: "))
for i in range(n):
    ID = input("Enter email ID: ")
    x.append(ID)
x = tuple(x)
for i in x:
    name, domain = i.split("@")
    names.append(name)
    domains.append(domain)
names = tuple(names)
domains = tuple(domains)

print("Your input: ", x)
print("Usernames: ", names)
print("Domain names: ", domains)
