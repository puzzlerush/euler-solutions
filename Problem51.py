def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def replace(lis, n):
    c = []
    for i in range(len(lis)):
        j = i + n
        if j > len(lis):
            j -= len(lis)
        lis[i:]
    
