#Write a Python program to count the number of characters (character frequency) in a string. Sample String: ‘google.com' 
#Expected Result: {'g': 2, 'o': 3, 'l': 1, 'e': 1,'.': 1, 'c': 1, 'm': 1} 
    
def frequency(s):
    d = {}
    for i in s:
        j = d.keys()
        if i in j:
            d[i]+=1
        else:
            d[i] = 1
    return d

print (frequency('google.com'))
