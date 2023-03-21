def GCD(x, y, reminder):

    if y == reminder:
        return x
    else:
        return GCD(y, x % y, reminder)

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
answer = []
start, end = 0, 0

candidate = []
if numbers[0] != 1:
    start, end = 2, numbers[0]+1
    candidate = [x for x in range(2, numbers[0]+1)]
else:
    start, end = 2, 3
    candidate = [2]

while numbers:
    num1 = numbers[0]
    num2 = numbers[1]
    new_candidate = []
    for x in candidate:
        gcd = 0
        if num1 % x == num2 % x:
            reminder = num1 % x
            new_candidate.append(x)

    candidate = new_candidate
    print(new_candidate)