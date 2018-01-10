def cyclelen(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    count = 1
    while True:
        if (10**count - 1) % n == 0:
            return count
        count += 1
x = {}    
for d in range(1, 1000):
    x[d] = cyclelen(d) 
    
print(max(x, key = x.get))
