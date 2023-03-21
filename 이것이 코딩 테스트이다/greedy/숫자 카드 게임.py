
# 초기 생각
# N, M = map(int, input().split())
# card = list()
# for row in range(N):
#     card.append(list(map(int, input().split())))
# answer = 0
# for row in range(N):
#     if row == 0:
#         answer = min(card[row])
#     else:
#         if answer < min(card[row]):
#             answer = min(card[row])
#
# print(answer)

# 조건문을 min, max 함수로 간단하게 대치가 가능

N, M = map(int, input().split())
result = 0
for row in range(N):
    card = list(map(int, input().split()))

    min_val = min(card)

    result = max(min_val, result)

print(result)

'''
항상 데이터를 저장하려는 습관이 있다. 비교 후 이용하지 않아도 된다면 
굳이 저장하지 않아도 된다는 것을 명심하자.
그리고 조건 분기가 복잡해진다면 내장 함수를 이용하는 방법을 택하자.
'''