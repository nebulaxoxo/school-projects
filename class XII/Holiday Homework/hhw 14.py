#Write a Python program to shuffle and print a specified list
from random import shuffle
def shuffle_list():
    n = int(input("How many entries would you like to make? "))
    l = []
    for i in range(n):
        j = input("Enter input: ")
        l.append(j)
    print("List created: \n", l)
    shuffle(l)
    print("List shuffled: \n", l)

shuffle_list()
