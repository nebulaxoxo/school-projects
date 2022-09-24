name = str(input("Enter name: "))
sub1 = int(input("Enter marks in first subject: "))
sub2 = int(input("Enter marks in second subject: "))
sub3 = int(input("Enter marks in third subject: "))
sub4 = int(input("Enter marks in fourth subject: "))
sub5 = int(input("Enter marks in fifth subject: "))
total = sub1 + sub2 + sub3 + sub4 +sub5
avg = total/5
if avg >= 50:
    print("PROMOTED.")
else:
    print("DETAINED.")

