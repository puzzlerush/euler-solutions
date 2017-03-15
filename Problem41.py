def pandigital(n, s):
    digits = list('123456789')[:n]
    if all(d in s for d in digits):
        if len(s) == n:
            return True
    return False
def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
from itertools import permutations
nums = [''.join(p) for p in permutations('1234567')] + [''.join(p) for p in permutations('1234')]
pandigitalprimes = []
for n in nums:
    if prime(int(n)):
        pandigitalprimes.append(int(n))
print(max(pandigitalprimes))
