def create_list():
    n = int(input("How many entries would you like to make? "))
    l = []
    for i in range(n):
        j = input("Enter input: ")
        l.append(j) 
    return l 
l1 = create_list()
def count_range(l, min, max):
	count = 0
	for x in l1:
		if min <= int(x) <= max:
			count += 1
	return count

print(count_range(l1,0,5))


