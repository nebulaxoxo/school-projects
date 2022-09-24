total = int(input("Enter number of classes held: "))
present = int(input("Enter number of classes attended: "))
percent = (present/total)*100
print("You have attended ", percent, "% of classes")
if percent >= 75:
    print("You may sit in the examinations.")
else: 
    a = str(input("Your attendance is less than the criteria. /n Is there a medical cause? (y/n): "))
    if a.lower() == 'y':
        print("You may sit in the examinations.")
    elif a.lower() == 'n':
        print("You may not sit in the examinations.")
    else:
        print("Invalid input.")

