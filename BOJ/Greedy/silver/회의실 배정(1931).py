n = int(input())
meetings = [[int(x) for x in input().split(' ')] for _ in range(n)]

meetings_sorted = sorted(meetings, key=lambda x: (x[0], x[1]))
possible_meetings = 0
stack = [meetings_sorted[0]]
for pos in range(1, len(meetings_sorted)):

    if stack[-1][1] > meetings_sorted[pos][1]:
        stack.pop()
        stack.append(meetings_sorted[pos])
    elif stack[-1][1] <= meetings_sorted[pos][0]:
        stack.append(meetings_sorted[pos])

print(len(stack))

