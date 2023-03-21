# first
# import sys
#
# N, M = map(int, sys.stdin.readline().split(' '))
# numbers = list(map(int, sys.stdin.readline().split(' ')))
# prefix = []
# temp_sum = 0
# cnt = 0
# for i in range(N):
#     temp_sum += numbers[i]
#     if temp_sum % M == 0:
#         cnt += 1
#     prefix.append(temp_sum)
#
# for i in range(1, N):
#
#     for j in range(N):
#         diff = 1
#         if i+j < N:
#             diff = prefix[i+j] - prefix[j]
#         if diff % M == 0:
#             cnt += 1
# print(cnt)
import sys

N, M = map(int, sys.stdin.readline().split(' '))
numbers = list(map(int, sys.stdin.readline().split(' ')))
cnt=0
numbers.insert(0,0)

for i in range(2, N+2):
    init_sum = 0
    for j in range(i):
        init_sum += numbers[j]

    for k in range(i, N+2):
        if init_sum % M == 0:
            cnt+=1
        if k > N:
            continue
        init_sum -= numbers[k-i+1]
        init_sum += numbers[k]

print(cnt)