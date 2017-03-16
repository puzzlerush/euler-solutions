pent = []
for n in range(1, 4000):
    pent.append(int((n*(3*n-1))/2))
p = dict.fromkeys(pent)
diffs = []
for j in range(2000):
    for k in range(j+1, 4000-1):
        if pent[j] + pent[k] in p and pent[k] - pent[j] in p:
            diffs.append(abs(pent[k]-pent[j]))
print(min(diffs))
            

