################################ my code ################################
import calendar

month, day, year = map(int, input().strip().split())

print (calendar.day_name[calendar.weekday(year, month, day)].upper())
############################# end of my code #############################