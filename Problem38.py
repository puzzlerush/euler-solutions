digits = list('123456789')
def pandigital(s):
    if all(d in s for d in digits):
        if len(s) == 9:
            return True
    return False

pandigits = []
for i in range(1, 10000):
    for n in range(2, 9 + 1):
        li = list(range(n))[1:]
        s = ''
        for l in li:
            s += str(i*l)
        if pandigital(s):
            pandigits.append(int(s))
print(max(pandigits))
