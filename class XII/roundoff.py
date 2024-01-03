import math

def round_float():
    float_number = float(input("Enter a float with 5 decimal digits: "))
    rounded_number = round(float_number, 2)
    print(f"The rounded value is: {rounded_number}")

round_float()
