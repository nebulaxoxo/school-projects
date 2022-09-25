x = input("Enter a sentence: ")
not_1 = x.lower().find('not')
poor = x.lower().find('poor')
if not_1 < poor and not_1 > 0 and poor > 0:
    x = x.replace(x[not_1:(poor+4)], 'good')
else:
    pass

print(x)