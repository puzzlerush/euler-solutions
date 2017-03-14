def frac():
    fractions = []
    for i in range(10, 100):
        for j in range(10, i):
            fractions.append('%s/%s' % (str(j), str(i)))
    return fractions

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
f = frac()
for frac in range(len(f)):
    f[frac] = f[frac].split('/')
numer = []
denom = []
for i in f:
    for d in digits:
        if d in i[0] and d in i[1] and len(set(i[0])) > 1 and len(set(i[1])) > 1:
            x = int(i[0].replace(d, ''))
            y = int(i[1].replace(d, ''))
            if x != 0 and y != 0:
                if x/y == int(i[0])/int(i[1]):
                    numer.append(int(i[0]))
                    denom.append(int(i[1]))
numeratorfinal = 1
for n in numer:
    numeratorfinal *= n
denominatorfinal = 1
for d in denom:
    denominatorfinal *= d

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(denominatorfinal//gcd(numeratorfinal, denominatorfinal))
