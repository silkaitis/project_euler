'''
You are given the following information,
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import datetime, timedelta

d = datetime(1901,1,1)
end = datetime(2000,12,31)

sun = 0

while d <= end:

    if (d.weekday() == 6) and (d.day == 1):
        sun += 1

    d += timedelta(days=1)

print('Number of Sundays from 1901 to 2000 is {}'.format(sun))
