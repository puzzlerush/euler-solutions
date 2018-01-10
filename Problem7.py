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
n = 0
while len(primes) <= 10000:
    n += 1
    if prime(n):
        primes.append(n)
print(primes[-1])
        
