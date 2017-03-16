def isPent(n):
    p1 = (1+((-1)**2-4*3*-2*n)**0.5)/6
    if p1 % 1 == 0:
        return True
    return False
def isHex(n):
    h1 = (1+((-1)**2-4*2*-n)**0.5)/4
    if h1 % 1 == 0:
        return True
    return False
n = 285 + 1
while True:
    tri = (n*(n+1))/2
    if isPent(tri) and isHex(tri):
        print(int(tri))
        break
    n += 1
