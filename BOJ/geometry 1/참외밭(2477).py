from collections import defaultdict

# 패턴을 찾는데는 성공했지만 패턴이 없는 경계조건에 대한 탐색이 부족했음
# 작은 패턴의 경우 모든 패턴을 검사해봐야함
# 이번 문제에서 찾지 못한 패턴은 내가 정의한 패턴이 입력에 없는 경우가 발생할 수도 있다는 것
# 예를 들면 순차적으로 입력된 방향 값을 저장한 리스트에서 [2,4] 라는 패턴을 찾도록 알고리즘을 구성
# 하지만 [4,2,3,1,4,2]순으로 입력된 경우 [2,4]라는 패턴을 찾을 수 없음
# 따라서 방향 값을 저장한 리스트를 2배로 늘려 [4,2,3,1,4,2]+[4,2,3,1,4,2]로 만들어 강제로 값을 찾게함
# 해결해야할 정보의 크기가 작아서 가능했지만 비효율적임
# 원형 큐로 해결해볼 수도 있을 것으로 판단됨

N = int(input())
infos = []
path = []
dists = []
path_dist = defaultdict(int)
for _ in range(6):
    direc, dist = map(int, input().split(' '))
    infos.append([direc, dist])
for info in infos:
    path.append(info[0])
    dists.append(info[1])
    path_dist[info[0]] += info[1]

path = path + [path[0]]
dists = dists + [dists[0]]
total_area = [path_dist[1], path_dist[3]]
minus_area = list()
minus_area_pattern = [[1, 3], [4, 1], [3, 2], [2, 4]]


for i in range(1, len(dists)):
    if [path[i-1], path[i]] in minus_area_pattern:
        minus_area = [dists[i-1], dists[i]]
        break

num_of_fruits = total_area[0] * total_area[1] - minus_area[0] * minus_area[1]
print(N*num_of_fruits)
