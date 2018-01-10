s = 0
for i in range(2, 300000):
    x = 0
    for digit in list(str(i)):
        x += int(digit)**5
    if x == i:
        s += i
print(s)
        
    
    
