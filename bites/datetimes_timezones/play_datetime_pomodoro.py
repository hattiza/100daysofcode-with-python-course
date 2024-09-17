#!python3

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

t.days
#4

t.seconds
#36000

t.hours
#Traceback (most recent call last):
    #File "<pyshell#119>", line 1, in <module> t.hours
#AttributeError: 'datetime.timedelta' object has no attribute 'hours'

t.seconds / 60 / 60
#10.0

t.seconds / 3600
#10.0


#########

eta = timedelta(days=4, hours=10)

today = datetime.today()

today
#datetime.datetime(2024, 9, 17, 14, 12, 19, 197404

today + eta
#datetime.datetime(2024, 9, 22, 0, 12, 19, 197404)

str(today + eta)
#'2024-09-22 00:12:19.197404'
