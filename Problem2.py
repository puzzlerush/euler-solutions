fib = [0,1]
even = []
while True:
    fib.append(fib[-1]+fib[-2])
    if fib[-1] > 4000000:
        break
for x in fib:
    if x % 2 == 0:
        even.append(x)
print(sum(even))
        
