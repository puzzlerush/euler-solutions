def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
primes = []
for x in range(2000000):
    if prime(x):
        primes.append(x)
print(sum(primes))
        
