#Write a Python function that takes two lists and returns True if they have at least one common member.
def create_list():
    n = int(input("How many entries would you like to make? "))
    l = []
    for i in range(n):
        j = input("Enter input: ")
        l.append(j) 
    return l   
def common_member():
    print("For list 1: ")
    l1 = create_list()
    print(l1)
    l2 = create_list()
    print(l2)
    for i in l1:
        for j in l2:
            if i == j:
                return True
        

print(common_member())
    
