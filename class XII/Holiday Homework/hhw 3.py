#Write a Python program to remove the nth index character from a nonempty string. 
def removen(s, n):
    output = s[:n] + s[n+1:]
    return output

print(removen('nandita', 1))