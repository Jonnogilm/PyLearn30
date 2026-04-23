import datetime
#Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.datetime.now()
print(f"Today is the {now.day}/{now.month}/{now.year}. It is exactly {now.hour}:{now.minute}")

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

#Today is 5 December, 2019. Change this time string to time.
time_string = '5 December, 2019'
time_obj = datetime.datetime.strptime(time_string, "%d %B, %Y")
print(type(time_obj))
print(time_obj)

#Calculate the time difference between now and new year.
print(dir(datetime))
now_time = now
new_years = datetime.datetime(2027, 1, 1)
print("Time between New Years and now is: ", (new_years-now_time))

#Calculate the time difference between 1 January 1970 and now.
unix_start_time = datetime.datetime(1970, 1, 1)
print("Difference is: ", now_time-unix_start_time)

#or can do
print("Difference to epoch is: ", now.timestamp())

#Think, what can you use the datetime module for? Examples:
        #For printing logs, or adding when users signed up for a database or completed a certain action, it can keep unix machines on the same page on what time is the real one. 
    #Time series analysis
        #Finance, you can write algorithems that sample data or certain indicators every minute, hour, day or anywhere in between.
    #To get a timestamp of any activities in an application
        #Also to stagger requests as you never want to bombard a web socket or mesh network of esp32s with requests when they are already transmitting other data.
    #Adding posts on a blog