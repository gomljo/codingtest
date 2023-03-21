N, M = map(int, input().split(' '))

never_heard = set()
never_heard_seen = list()

for _ in range(N):
    never_heard.add(input())

for _ in range(M):
    name = input()
    if name in never_heard:
        never_heard_seen.append(name)
never_heard_seen.sort()
print(len(never_heard_seen))
print('\n'.join(never_heard_seen))