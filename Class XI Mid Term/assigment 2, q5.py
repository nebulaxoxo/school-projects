ans = str(input("Press C to convert celsius to fahrenheit. /n Press F to convert fahrenheit to celsius."))
if ans.lower() == 'c':
    temp = int(input("Enter temperature (in celsius): "))
    fahren = (9*temp + (32*5))/5
    print(temp, "℃ is ", fahren, "℉.")
elif ans.lower() == 'f':
    temp = int(input("Enter temperature (in fahrenheit): "))
    celsius = (5*(temp - 32))/9
    print(temp, "℉ is ", celsius, "℃.")
else:
    print("Invalid input.")

