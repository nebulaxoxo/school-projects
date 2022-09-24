flag = 0
for i in range(3):
    pwd = input("Enter the password: ")
    if pwd == "SECRET":
        print("Welcome!")
        flag = 1
        break
    else:
        print("Wrong password! \n")

if flag == 0:
    print("You can not enter the house.")
    
    

