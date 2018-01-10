def pfac(n):
    primefac = []
    for d in range(2, int(n**0.5) + 1):
        while n % d == 0:
            primefac.append(d)
            n //= d
    if n > 1:
        primefac.append(n)
    return len(set(primefac))
i = 1
while True:
    if pfac(i) == 4 and pfac(i+1) == 4 and pfac(i+2) == 4 and pfac(i+3) == 4:
        print(i)
        break
    i += 1
