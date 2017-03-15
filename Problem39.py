def valid(a, b, c):
    if a + b > c or b + c > a or a + c > b:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return True
    return False

d = {}
for p in range(3, 1000 + 1):
    validsolutions = 0
    for a in range(1, p//2):
        for b in range(1, p - a):
            c = p - a - b
            if valid(a, b, c):
                validsolutions += 1
    d[p] = validsolutions
print(max(d, key=d.get))
