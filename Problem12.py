def numOfFactors(n):
    factors = 0
    for i in range(1, int(n+1)):
        if n%i == 0:
            factors += 1
    return factors
        
i = 0
while True:
    i += 1
    x = i*(i+1)//2
    if numOfFactors(x) > 500:
        print(x)
        break
    
    
    
