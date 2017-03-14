def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def trunc(string):
    s = string
    left = []
    right = []
    t = set()    
    while len(s) > 0:
        left.append(int(s))
        s = s[1:]
    s = string
    while len(s) > 0:
        right.append(int(s))
        s = s[:-1]
    for l in left:
        t.add(l)
    for r in right:
        t.add(r)
    return t
truncprimes = []
i = 8
while len(truncprimes) < 11:
    if all(prime(x) for x in trunc(str(i))):
         truncprimes.append(i)
    i += 1
print(sum(truncprimes))
