import matplotlib.pyplot as plt
import numpy as np
a = int(input("Enter range start point (x): "))
b = int(input("Enter range end point (x): "))
print("Objective: To produce a *straight* line with user inputs.")
c = int(input("What exponent would you like the y-range to be? (relative to x): "))
x = range(a,b)
y = [value*c for value in x]
plt.plot(x,y, ':',color = 'goldenrod', linewidth = 2)
n = str(input("Enter x-axis label: "))
z = str(input("Enter y-axis label: "))
q = str(input("Enter Title for graph: "))
plt.xlabel(n)
plt.ylabel(z)
font = {'family':'fantasy','color':'darkslategray', 'size': 20}
plt.title(q, fontdict=font)
plt.show()

