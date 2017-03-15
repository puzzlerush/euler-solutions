def isTriangleNum(n):
    t1 = (-1 + (1**2 - 4*1*-2*n)**0.5)/2
    t2 = (-1 - (1**2 - 4*1*-2*n)**0.5)/2
    if t1 % 1 == 0 or t2 % 1 == 0:
        return True
    return False

def getWordVal(s):
    val = 0
    for c in s:
        val += ord(c) - 64
    return val
trianglewords = 0
words = open('p042_words.txt').read().replace('"', '').split(',')
for w in words:
    if isTriangleNum(getWordVal(w)):
        trianglewords += 1
print(trianglewords)
