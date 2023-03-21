from itertools import combinations_with_replacement, product
from collections import Counter
# def dfs(n, info, idx, scores):
#     if n < 1 or len(info)-1 <= idx:
#         return scores
#     score = scores[0]
#     if info[idx] != 0:
#         new_score_apeach_win = [score[0] + (10 - idx), score[1]]
#         scores.insert(0, new_score_apeach_win)
#
#     idx += 1
#     scores = dfs(n, info, idx, scores)
#
#     new_score_lion_win = [score[0], score[1] + (10 - idx)]
#     scores.insert(0, new_score_lion_win)
#
#     n -= info[idx] + 1
#     scores = dfs(n, info, idx, scores)
#
#     return scores
#
# def solution(n, info):
#     answer = []
#
#     scores = [[0, 0]]
#     # [apeach, lion]
#     scores = dfs(n, info, 0, scores)
#     print(scores)
#     sorted_list = sorted(scores, key=lambda x : x[0]-x[1])
#     print(sorted_list)
#
#     return answer


def solution(n, info):
    answer = [-1]
    maxGap = -1e9
    candidates = list(combinations_with_replacement(range(0, 11), n))
    candidate = list(product([1,2,3,4], repeat=2))
    print(candidate)
    print(candidates)
    for candidate in candidates:
        info2 = [0] * 11
        apeach, lion = 0, 0

        for score in candidate:
            info2[10 - score] += 1

        for score, (a, l) in enumerate(zip(info, info2)):
            if a == l == 0:
                continue
            elif a >= l:
                apeach += (10 - score)
            else:
                lion += (10 - score)

        if lion > apeach:
            gap = lion - apeach
            if gap > maxGap:
                maxGap = gap
                answer = info2

    return answer

n=5
info=[2,1,1,1,0,0,0,0,0,0,0]
result=[0,2,2,0,1,0,0,0,0,0,0]

ans = solution(n, info)
print(ans)