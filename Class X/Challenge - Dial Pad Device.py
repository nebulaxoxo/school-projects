from datetime import date as d
import datetime as dt

button_pressed = 0

button_pressed = input("Please press a button")
if button_pressed == "1":
    print(d.today())
elif button_pressed == "2":
    print(dt.datetime.now())
else:
    print("Wrong input entered")


