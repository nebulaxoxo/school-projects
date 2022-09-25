x = input("Enter a string: ")
alpha = x[0] #first character
out = x.replace(alpha, '$')
out_final = alpha + out[1:]
print(out_final)
