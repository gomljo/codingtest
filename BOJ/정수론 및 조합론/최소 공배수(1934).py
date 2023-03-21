def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)


N = int(input())
numbers = []
for _ in range(N):
    a, b = map(int, input().split(' '))
    numbers.append([a,b])
for number in numbers:
    a = number[0]
    b = number[1]
    gcd = GCD(a, b)
    lcm = gcd * (a // gcd) * (b // gcd)
    print(lcm)