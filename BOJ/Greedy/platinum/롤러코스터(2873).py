def dfs(start_coord, enjoy_map, visited, answer, answers):
    up = {'U': [-1, 0]}
    left = {'L': [0, -1]}
    right = {'R': [0, 1]}
    down = {'D': [1, 0]}
    if start_coord == [len(enjoy_map), len(enjoy_map[0])]:
        return answer

    for d in [up, down, left, right]:
        direction, coord = list(d.keys())[0], list(d.values())[0]
        x = start_coord[0] + coord[0]
        y = start_coord[1] + coord[1]
        if (x < 0 or x > len(enjoy_map)-1) or (y < 0 or y > len(enjoy_map[0])-1):
            continue
        if visited[x][y] == 0:
            visited[x][y] = 1
            new_answer = answer + direction
            answers.append(dfs([x, y], enjoy_map, visited, new_answer, answers))
            visited[x][y] = 0

    return answers


r, c = map(int, input().split(' '))
park = [[int(x) for x in input().split(' ')] for _ in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]
visit[0][0] = 1
start = [0, 0]
ans = ''
result = []
dfs(start, park, visit, ans, result)
print(result)



