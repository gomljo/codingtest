N, K = map(int, input().split(' '))
scores = [int(x) for x in input().split(' ')]

scores.sort(reverse=True)
print(scores[:K][-1])