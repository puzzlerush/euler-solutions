import datetime
s  = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        d = datetime.date(y, m, 1)
        if d.weekday() == 6:
            s += 1
print(s)
