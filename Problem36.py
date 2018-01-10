def palindrome(s):
    if s == s[::-1]:
        return True
    return False
dbpal = 0
for i in range(1, 1000000):
    if palindrome(str(i)) and palindrome("{0:b}".format(i)):
        dbpal += i
print(dbpal)
