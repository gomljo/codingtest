num_of_towers = int(input())
height_of_tower = [int(i) for i in input().split(' ')]

stack = []
receive = []
for idx, signal in enumerate(reversed(height_of_tower)):

    # if not stack:
    #     stack.append(signal)
    #     continue
    if stack and stack[-1] < signal:
        temp_receive = [str(num_of_towers - idx)] * len(stack)
        temp_receive.extend(receive)
        receive = temp_receive
        stack = []
    stack.append(signal)

rest = ['0'] * len(stack)
rest.extend(receive)
receive = ' '.join(rest)
print(receive)
print(len(receive))

# import sys
#
# n = int(sys.stdin.readline())
# tower = list(map(int, sys.stdin.readline().split()))
# stack = []
# goto = [0] * n
#
# for i in range(n):
#     t = tower[i]
#     while stack and tower[stack[-1]] < t:
#         stack.pop()
#     if stack:
#         goto[i] = stack[-1] + 1
#     stack.append(i)
#
# print(' '.join(list(map(str, goto))))