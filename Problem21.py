def d(n):
    x = []
    for i in range(1, n):
        if n%i == 0:
           x.append(i)
    return sum(x)

amic = []
for i in range(1, 10001):
    if i == d(d(i)) and i != d(i):
        if i not in amic and d(i) not in amic:
            amic.append(i)
            amic.append(d(i))
print(sum(amic))


