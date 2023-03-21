N, M = map(int, input().split(' '))

set_s = set()

for i in range(N):
    set_s.add(input())

strings = []
for j in range(M):
    strings.append(input())

cnt = 0
for string in strings:
    if string in set_s:
        cnt+=1

print(cnt)