import sys
from collections import Counter
n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

print(round(sum(numbers) / n))
numbers.sort()
print(numbers[n//2])
cnt_res = Counter(numbers).most_common(2)
if len(cnt_res) > 1:
    if cnt_res[0][1] == cnt_res[1][1]:
        print(cnt_res[1][0])
    else:
        print(cnt_res[0][0])
else:
    print(cnt_res[0][0])
print(numbers[-1] - numbers[0])
