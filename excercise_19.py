import datetime
import time
def clock():
    datetime_object = datetime.datetime.now()
    datetime_object = datetime_object.strftime("%d/%m/%Y, %H:%M:%S")
    print(datetime_object)
    time.sleep(1)
    return True

while clock:
    clock()



