def collatz(n):
    i = 0 
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1
        i += 1
    return i + 1
termNums = {}
for x in range(2, 1000000):
    termNums[x] = collatz(x)
print(max(termNums, key = termNums.get))
