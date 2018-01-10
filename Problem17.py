single = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
teen = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
double = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
st = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

def count(n):
    if n < 10:
        return len(single[n])
    elif n < 20:
        return len(teen[n])
    elif n >= 20 and n < 100:
        return len(double[n//10]) + len(single[n%10])
    elif n%100 == 0:
        return len(single[n//100]) + 7
    elif n%100 < 20:
        return len(single[n//100]) + 7 + 3 + len(st[n%100])
    else:
        return len(single[n//100]) + 7 + 3 + len(double[(n%100)//10]) + len(single[n%10])
            
total = 0
for i in range(1, 1000):
    total += count(i)
print(total+11)
