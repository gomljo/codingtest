n = int(input())
p = [int(x) for x in input().split(' ')]

p.sort()

total = sum(p)

answer = total
last_person = total
for i in reversed(p):
    last_person -= i
    answer += last_person

print(answer)