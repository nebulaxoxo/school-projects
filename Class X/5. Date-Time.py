from datetime import datetime as dt
a = dt.now()
print ("Today's date is [mm/dd/yy]: ", a.strftime("%D"))
print("Time right now is: ", a.strftime("%H:%M:%S"))

