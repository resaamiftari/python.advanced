import datetime

from main5 import currentTime

timeObj=datetime.time(12,30,45,651651)

print(timeObj.hour)
print(timeObj.minute)
print(timeObj.second)
print(timeObj.microsecond)

dateobj=datetime.date(2010,1,1)

print(dateobj.year)
print(dateobj.month)
print(dateobj.day)

specificDate=datetime.datetime(2010,1,1,4,25,54,54545)
formatimiDates = specificDate.strftime("%Y-%m-%d")
print(formatimiDates)

utc=datetime.datetime.now(datetime.timezone.utc)
print(utc)

currentTime=datetime.timedelta(hours=3)

costumTime=utc.replace(tzinfo=datetime.timezone(currentTime))
print(costumTime)

