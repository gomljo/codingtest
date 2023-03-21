import sys
n = int(input())
nums = sys.stdin.readline().split(' ')
numbers = set()
for i in nums:
    numbers.add(int(i))
numbers = sorted(numbers)

answer = dict()
for i in range(len(numbers)):
    answer[numbers[i]] = i

for num in nums:
    print(answer[int(num)], end=' ')