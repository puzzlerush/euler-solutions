import itertools
p = itertools.permutations('0123456789')
count = 0
for i in p:
    if count == 999999:
        print(''.join(i))
    count += 1
