#Write a Python program to sum all the items in a list.
def sum_list(*n):
    l = []
    for i in n:
        l.append(i)
    out = sum(l)
    print(out)

sum_list(10,20,30,12,8,0)