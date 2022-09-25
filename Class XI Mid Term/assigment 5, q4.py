from re import X


x = input("Enter a string: ")
a = x[-3:]
if len(x) >= 3:
    if a.lower() == 'ing':
        out = x + 'ly'
    else:
        out = x + 'ing'
else:
    out = x

print(out)
