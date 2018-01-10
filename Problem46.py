def isOddComp(n):
    if n % 2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False
def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primeSquares(n):
    primes = []
    for i in range(2, n):
        if prime(i):
            primes.append(i)
    squares = []
    for i in range(1, n):
        if i**0.5 % 1 == 0:
            squares.append(i)
    for p in primes:
        for s in squares:
            if p + 2*s == n:
                return True
    return False
i = 1
while True:
    if isOddComp(i) and not primeSquares(i):
        print(i)
        break
    i += 1

