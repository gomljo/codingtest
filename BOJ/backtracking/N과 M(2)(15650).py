def dfs(start, end, visited, seq, max_length):
    if len(seq) == max_length:
        print(' '.join(map(str, seq)))
        return

    for i in range(start, end):

        if visited[i-1] != 1:
            visited[i-1] = 1
            seq.append(i)
            new_start = i + 1
            dfs(new_start, end, visited, seq, max_length)
            seq.pop()
            visited[i-1] = 0


N, M = map(int, input().split(' '))
visit = [0] * N
sequence = []
dfs(1, N+1, visit, sequence, M)
