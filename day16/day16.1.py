import datetime

# datetime is a large module used for common date and time queries
print(dir(datetime)) # shows available functions

now = datetime.datetime.now()
print(now.day) # .month .year .hour .second
print(now.second)

print(now.timestamp()) # unix epoch timestamp that are seconds since 1970 UTC

# can also specify a time to start at so: new_year = datetime(2020, 1, 1)
# strtime formats the timestamps pretty easily
print(now.strftime("%d/%m/%Y, %H:%M:%S")) # there are also symbols for timezones, weekdays, and many many more things

# strptime takes a string and a 'format code' to return a datetime object (for db most likely)
canadian_date = '15 March, 2008'
date_obj = now.strptime(canadian_date, '%d %B, %Y')
print('Your date obj is: ', date_obj)

# from datetime import date
# can use to save a date obj
d = datetime.date(2008, 5, 3)

# can also use to get todays date but I think now is better:
print(datetime.date.today().month)

# use a time obj to save times
a = datetime.time(5,6, 3, 20)
print(type(a))
print(a)

# use timedelta to find the time between two events
a = datetime.timedelta(4,5)
b = datetime.timedelta(2, 10000)
c = a-b
print(c)