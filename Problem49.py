from itertools import permutations
def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  
def pp(s):
    li = []
    for p in permutations(s):
        n = int(''.join(p))
        if prime(n) and len(str(n)) == len(s):
            li.append(n)
    if li[0] + 3330 in li and li[0] + 2*3330 in li:
        return True
    return False
primes = []
for i in range(1000, 9999 + 1):
    if prime(i):
        primes.append(i)
for p in primes:
    if pp(str(p)) and p != 1487:
        print(str(p)+str(p+3330)+str(p+2*3330))
