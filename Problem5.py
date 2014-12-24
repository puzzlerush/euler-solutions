def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
def lcm(a,b):
    lcm = a*b // gcd(a,b)
    return lcm
print(lcm(11,lcm(12,lcm(13,lcm(14,lcm(15,lcm(16,lcm(17,lcm(18,lcm(19,lcm(20,20)))))))))))
