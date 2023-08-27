#Write a Python program to create a dictionary from two lists without losing duplicate values. Sample data: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
#Expected Output: defaultdict(<class 'set'>, {'Class-V':{1}, 'Class-VI':{2}, 'Class-VII':{2}, 'Class- VIII':{3}})

l1 =  ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
l2 = [1, 2, 2, 3]
d = {}
for key in l1:
    for value in l2:
        d[key] = value
        l2.remove(value)
        break

print("Resultant dictionary is : " + str(d))