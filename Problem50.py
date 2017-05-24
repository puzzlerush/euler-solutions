def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
primelist = []
for i in range(2, 1000000):
    if prime(i):
        primelist.append(i)
def lengthsum(length):
    maxprime = 0
    for i in range(1000000):
        t = sum(primelist[i:i+length])
        if t > 1000000:
            break
        if prime(t):
            maxprime = t
    return maxprime
p = []
for i in range(1000, 0, -1):
    s = lengthsum(i)
    if s:
        p.append(i)        
print(lengthsum(max(p)))
