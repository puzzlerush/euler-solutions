def factorial(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p
digit_factorials = []
for i in range(10, 2540160 + 1):
    dfsum = 0
    for digit in str(i):
        dfsum += factorial(int(digit))
    if dfsum == i:
        digit_factorials.append(i)
print(sum(digit_factorials))
