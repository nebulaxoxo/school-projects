#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
#Sample Words: red, white, black, red, green, black Expected Result: black, green, red, white, red 

def sorter():
    s = input('Enter a string: ')
    l1 = s.split(',')
    x = sorted(set(l1))
    x = ','.join(x)
    print(x)

sorter()