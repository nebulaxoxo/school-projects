#Write a Python program to remove duplicates from a list. 
#a = [10,20,30,20,10,50,60,40,80,50,40]

def remove_dupli(*n):
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    print (l)

remove_dupli(10,20,30,20,10,50,60,40,80,50,40)