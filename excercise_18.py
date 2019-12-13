import datetime
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
datetime_object = datetime.datetime.now()
day = datetime_object.weekday()
datetime_object = datetime_object.strftime("%d/%m/%Y, %H:%M:%S")
print(weekDays[day])
print(datetime_object)

