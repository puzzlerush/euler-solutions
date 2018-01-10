s = 0
for i in range(1001, 1, -2):
    s += i*i
    s += i*i - (i - 1)
    s += i*i - 2*(i - 1)
    s += i*i - 3*(i - 1)
print(s + 1)
        
    
