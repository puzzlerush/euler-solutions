def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

c = {}
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n, count = 0, 0
        while True:
            if prime(n**2 + a*n + b):
                 count += 1
            else:
                c[count] = a*b
                break
            n += 1
k = []
for key in c.keys():
    k.append(key)
print(c[max(k)])
                
                
            
