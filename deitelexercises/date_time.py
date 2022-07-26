from datetime import datetime,timedelta

d1= datetime.now()
d2= datetime(2021, 5, 27)
diff = d1 - d2
# print(d.year)
print(diff)

t = timedelta(weeks = 1)
print (d1 + t)


# converting string to time
date_from_str = datetime.strptime("2022-02-02", "%Y-%m-%d")
print(date_from_str.year)

d = datetime.now()
print(d.strftime('%A %d %B %Y'))

