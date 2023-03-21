import sys
from bisect import bisect, bisect_left

N, H = map(int, sys.stdin.readline().split(' '))

even = []
odd = []

for i in range(N):
    obstacle = int(input())
    if i % 2 ==0:
        even.append(obstacle)
    else:
        odd.append(obstacle)
num_of_destroy = []
even.sort()
odd.sort()

for j in range(0, H):
    e_cnt = len(even) - bisect(even, j)
    o_cnt = len(odd) - bisect_left(odd, H-j)
    num_of_destroy.append(o_cnt+e_cnt)
num_of_destroy.sort()
print(min(num_of_destroy), bisect(num_of_destroy, min(num_of_destroy)))