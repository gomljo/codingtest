def dfs(end, visited, seq, max_length):
    if len(seq) == max_length:
        print(' '.join(map(str, seq)))
        return

    for i in range(1, end+1):

        if visited[i-1] != 1:
            seq.append(i)
            dfs(end, visited, seq, max_length)
            seq.pop()


N, M = map(int, input().split(' '))
visit = [0] * N
sequence = []
dfs(N, visit, sequence, M)
