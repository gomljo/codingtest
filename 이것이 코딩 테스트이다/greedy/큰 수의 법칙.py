
answer = []

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first_max = data[0]
second_max = data[1]

pattern = [first_max] * k
pattern.append(second_max)

if m % (k+1)==0:
    answer = pattern * (m // (k+1))
else:
    answer = pattern * ((m // k+1)+1)
    answer = answer[:m]

print(sum(answer))