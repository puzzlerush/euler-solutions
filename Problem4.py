n = 0
i = 999
while i >= 100:
    j = i
    while j >= 100:
        x = i*j
        if x > n:
            p = str(i*j)
            if p == p[::-1]:
                n = i*j
        j-=1
    i-=1
print(n)
