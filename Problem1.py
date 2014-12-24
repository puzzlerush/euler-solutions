x = []
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        x.append(n)
print(sum(x))
