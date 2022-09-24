num = str(input("Enter a number: "))
list = list(num)
list2 = list[::-1] #Reversing
if list == list2:
    print("It is a palindrome.")
else: 
    print("It is not a palindrome.")
    