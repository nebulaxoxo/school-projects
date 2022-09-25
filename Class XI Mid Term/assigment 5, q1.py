f = str(input("Enter first name: "))
m = str(input("Enter middle name (type nil if none): "))
l = str(input("Enter last name: "))
first = f[0].upper()
last = l.title()
if m.lower() == 'nil':
    name = first + '.' + last
else: 
    middle = m[0].upper()
    name = first + '.' + middle + '.' + last


print(name)