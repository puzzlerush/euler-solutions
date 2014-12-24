s = str(2**1000)
s = list(s)
i = 0
while i < len(s):
    s[i] = int(s[i])
    i += 1
print(sum(s))
