import math

N, M, K = map(int, input().split(' '))
standard = 0
if K % 2==0:
    standard = K**2 // 2
else:
    standard = K**2 // 2 + 1
board = []
prefix = [[[0, 0] for _ in range(M+1)]]
for i in range(N):
    row = list(input())
    temp_prefix = prefix[i][:]
    temp_cnt = [0, 0]
    res_temp_cnt = [0,0]
    for j in range(M):
        if row[j] == 'B':
            temp_cnt[0] += 1
        else:
            temp_cnt[1] += 1
        for k in range(len(temp_cnt)):
            res_temp_cnt[k] = prefix[i][j+1][k] + temp_cnt[k]
        temp_prefix[j+1] = res_temp_cnt[:]
    prefix.append(temp_prefix[:])
min_change = math.inf
for i in range(len(prefix)):
    print(prefix[i])
for i in range(0,N-K+1):

    for j in range(0, M-K+1):
        s_x, s_y, e_x, e_y = i+1, j+1, i+K, j+K
        total_b, total_w = prefix[e_x][e_y][0], prefix[e_x][e_y][1]
        print(s_x, s_y)
        print(e_x, e_y)
        print(prefix[e_x][e_y])
        print(prefix[e_x][s_y-1])
        print(prefix[s_x-1][e_y])
        print(prefix[s_x-1][s_y-1])
        outside1_b, outside1_w = prefix[e_x][s_y-1][0], prefix[e_x][s_y-1][1]
        outside2_b, outside2_w = prefix[s_x-1][e_y][0], prefix[s_x-1][e_y][1]
        redundant_b, redundant_w = prefix[s_x-1][s_y-1][0], prefix[s_x-1][s_y-1][1]
        b_cnt = total_b-outside1_b-outside2_b+redundant_b
        w_cnt = total_w-outside1_w-outside2_w+redundant_w
        print(b_cnt, w_cnt)
        more = max(b_cnt, w_cnt)
        if min_change > abs(standard-more):
            min_change = abs(standard-more)
print(min_change)