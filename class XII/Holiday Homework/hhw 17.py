#Write a Python program to replace the last element in a list with another list. 
#Sample data: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

def create_list():
    n = int(input("How many entries would you like to make? "))
    l = []
    for i in range(n):
        j = input("Enter input: ")
        l.append(j) 
    return l 
l1 = create_list()
l2 = create_list()
def element_replace(l1, l2):
    '''l1 = [1, 3, 5, 7, 9, 10]
    l2 = [2, 4, 6, 8]'''
    l1[-1:] = l2
    print(l1)

element_replace(l1, l2)