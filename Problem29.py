x = set()
for a in range(2, 101):
    for b in range(2, 101):
        x.add(a**b)
print(len(x))
