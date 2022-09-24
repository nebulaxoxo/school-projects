import datetime
realtime = datetime.datetime.now().date()
year = realtime.strftime("%Y")
service = int(input("Enter your year of service: "))
salary = int(input("Enter your salary amount (in rupees): "))
serviceyears = int(year) - service
print("You have been a part of our organisation for ", serviceyears, " years.")
if serviceyears >=5:
    bonus = (5/100)*salary
    net = salary + bonus
    print("Your net salary is: ", net)
else:
    print("Your net salary is: ", salary)
