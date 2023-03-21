# 테스트 케이스의 수를 입력
import math

N = int(input())

# 리스트는 순서대로 x, y, 거리를 나타낸다.
jo = [0, 0, 0]
beak = [0, 0, 0]
answer = []
for _ in range(N):

    jo[0], jo[1], jo[2], beak[0], beak[1], beak[2] = map(int, input().split(' '))

    # 조규현과 백승환의 x,y 좌표는 원의 중심점이고 적까지의 거리는 원의 반지름이 된다.
    # 결국, 두 원의 교점을 구하는 문제이다.
    # 케이스는 총 4개이다.
    # 케이스 1: 교점이 존재하지 않는다.
    # 케이스 2: 외접한다(교점이 1개 존재)
    # 케이스 3: 서로 겹치는 부분이 일부 존재한다(교점이 2개 존재)
    # 케이스 4: 서로 겹친다(무한대의 교점이 존재)
    # 케이스 5: 내접한다(교점이 1개 존재)

    dist = (math.sqrt((jo[0] - beak[0])**2 + (jo[1]-beak[1])**2))
    inter_dist = abs(jo[2] - beak[2])

    if dist == 0 and jo[2] == beak[2]:
        answer.append('-1')
    elif dist == inter_dist or dist == jo[2] + beak[2]:
        answer.append('1')
    elif inter_dist < dist < jo[2] + beak[2]:
        answer.append('2')
    else:
        answer.append('0')

print('\n'.join(answer))