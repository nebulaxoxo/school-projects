#Write a Python program to print the even numbers from a given list. 
#Sample List: [1, 2, 3, 4, 5, 6, 7,8, 9] 
#Expected Result: [2, 4, 6, 8]

def create_list():
    n = int(input("How many entries would you like to make? "))
    l = []
    for i in range(n):
        j = input("Enter input: ")
        l.append(j) 
    return l 

l = create_list()
def even_numbers(l):
    for i in l: 
        if int(i)%2 == 0:
            print (i)

even_numbers(l)
