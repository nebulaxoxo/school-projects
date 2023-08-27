#Write a Python program to get the largest number from a list.
def max_list(*n):
    l = []
    for i in n:
        l.append(i)
    out = max(l)
    print(out)

max_list(10,20,30,12,8,0)
