from collections import deque

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

print(maze)


def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True
    while queue:

        for i in queue:
            if not visited[i]:
