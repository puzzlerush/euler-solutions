def abundant(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i}
            result |= {div}
    if sum(result) - n > n:
        return True
    return False

abundantnums = []
for i in range(1, 28124):
    if abundant(i):
        abundantnums.append(i)
        
total = 0
for i in range(1, 28124):
    summable = False
    for a in abundantnums:
        if a > i:
            break
        if abundant(i - a):
            summable = True
            break
    if not summable:
        total += i
print(total)

                

