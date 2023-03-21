def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)


A, B = map(int, input().split(' '))
gcd = GCD(A, B)
lcm = gcd * (A // gcd) * (B // gcd)
print(gcd)
print(lcm)