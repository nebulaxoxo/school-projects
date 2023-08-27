#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
#Sample String: 'restart' Expected Result: 'resta$t' 
def change_dollar(s):
    x = s[0]
    a = s.replace(x, '$')
    s = x + a[1:]
    return s
print(change_dollar('restart'))

