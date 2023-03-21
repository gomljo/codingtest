import sys
input=sys.stdin.readline

n = int(input())
counting = [0] * 10001

for _ in range(n):
    counting[int(input())] += 1

for j in range(len(counting)):
    if counting[j] != 0:
        for k in range(counting[j]):
            print(j)