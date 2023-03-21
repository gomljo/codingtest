N, K = map(int, input().split(' '))
coins = []

for i in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0
while K != 0:
    coin = coins.pop(0)

    coin_cnt = K // coin
    if coin_cnt != 0:
        K -= coin * (K // coin)
        cnt += coin_cnt
print(cnt)