def factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append([i, n//i])
    return factors

def pandigital(n):
    f = factors(n)
    for subset in range(len(f)):
        mmp = str(f[subset][0]) + str(f[subset][1]) + str(n)
        if '1' in mmp and '2' in mmp and '3' in mmp and '4' in mmp and '5' in mmp and '6' in mmp and '7' in mmp and '8' in mmp and '9' in mmp and len(mmp) == 9:
            return True
    return False
s = set()
for i in range(10000):
    if pandigital(i):
        s.add(i)
print(sum(s))        

            
    
