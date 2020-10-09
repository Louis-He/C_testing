import datetime
t = datetime.datetime(2020, 7, 9, 22, 6, 2)
print((t - datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds())
