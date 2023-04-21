def modify(*lst):
    num = list(lst)
    for i in range(0, len(num)): 
        try:
            if num[i]%5 == 0:
                num[i] = 0
            else:
                num[i] = 1
        except TypeError:
            print("Invalid Input. Check Data type.")
    print("Your list:\n",num)

modify(1,5,10,2,4,6,20)
modify(50, 435, 43, 756, 12, 95)