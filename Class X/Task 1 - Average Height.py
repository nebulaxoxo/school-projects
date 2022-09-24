height = [140,154,181,173,176,169,153,163,140,158]

sum = 0             # Specifying Variable 1        
average = 0         # Specifying Variable 2

for i in height:    # Loop start
    sum = sum + i   # Adding every consequent height in list 
# Average = sum of values/number of values
average = sum/len(height)    # len for total 'number' of values in list
print(average)      # printing output


