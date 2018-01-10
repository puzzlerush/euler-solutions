def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def circulations(li):
    p = []
    for i in range(len(li)):
        li = li[-1:] + li[:-1]
        p.append(int(''.join(li)))
    return p
circularprimes = 0
for i in range(2, 1000000):
    intlist = list(str(i))
    if all(prime(j) for j in circulations(intlist)):
        circularprimes += 1
print(circularprimes)
        
        
    
