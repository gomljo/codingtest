def solution(N, road, K):
    def dfs(start, node_dict, dist, res, visit):
        # print('start node', start, 'path info', node_dict[start])
        for dest in node_dict[start].keys():
            # print('start at:', start, ', destination to: ', dest)
            if visit[dest - 1] == 0:
                # print('not yet visited destination', dest)
                for path_dist in node_dict[start][dest]:
                    # print('before path dist', dist)

                    if dist + path_dist <= K:
                        # print(start, dest)
                        new_dist = dist + path_dist
                        # print('total distance from 1 to ', start, ' to', dest, ': ' ,new_dist)
                        visit[dest - 1] = 1
                        res[dest - 1] = 1
                        res = dfs(dest, node_dict, new_dist, res, visit)
                        visit[dest - 1] = 0
        return res

    node_dict = dict()
    for node in range(1, N + 1):
        node_dict[node] = dict()
        for r in road:
            if node == r[0]:
                if r[1] in node_dict[node].keys():
                    node_dict[node][r[1]].extend([r[2]])
                else:
                    node_dict[node][r[1]] = [r[2]]
            elif node == r[1]:
                if r[0] in node_dict[node].keys():
                    node_dict[node][r[0]].extend([r[2]])
                else:
                    node_dict[node][r[0]] = [r[2]]

    temp_answer = [0] * N
    temp_answer[0] = 1
    for key in node_dict[1].keys():
        visit = [0] * N
        visit[0] = 1
        for distance in node_dict[1][key]:
            if distance <= K:
                visit[key - 1] = 1
                temp_answer[key - 1] = 1
                dfs(key, node_dict, distance, temp_answer, visit)
    # print(temp_answer)
    return sum(temp_answer)
# 마지막 케이스 시간초과가 발생
# 이유는 딕셔너리의 생성인듯 하여 기존의 딕셔너리 구조를 변경하기로 함
# 기존의 딕셔너리 구조
# node_dict[출발지][도착지] = [거리1, 거리2, ...]
# 변경된 딕셔너리 구조
# node_dict[(출발지, 도착지)] = [거리1, 거리2, ...]