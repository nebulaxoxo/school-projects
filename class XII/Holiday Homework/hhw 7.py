#Write a Python program to print the following floating numbers with no decimal places.
def integer(n):
    out = '{:.0f}'.format(n)
    print(out)

integer(12.99)
integer(3.1498361276)
integer(5.0)
