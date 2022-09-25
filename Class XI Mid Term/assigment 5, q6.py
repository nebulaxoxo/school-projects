#Write a program to find the number of vowels, consonents, digits and white space characters in a string.
x = input("Enter a string: ")
#vowels
vowels = 'aeiouAEIOU'
vowcount = 0
for i in x:
    for j in vowels:
        if i.lower() == j:
            vowcount += 1

print("Number of vowels: ", vowcount)

#consonants
consonants = 'bcdfghjklmnpqrstvwxyz'
conscount = 0
for i in x:
    for j in consonants:
        if i.lower() == j:
            conscount += 1

print("Number of consonants: ", conscount)

#digits
digits = '012345689'
digicount = 0
for i in x:
    for j in digits:
        if i == j:
            digicount += 1

print("Number of digits: ",digicount)

#Spaces
spaces = " "
spacecount = 0
for i in x:
    if i == spaces:
        spacecount += 1

print("Number of white spaces: ", spacecount)

