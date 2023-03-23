def dfs(start, end, visited, seq, max_length):
    if len(seq) == max_length:
        print(' '.join(map(str, seq)))
        return

    for i in range(start, end):

        if visited[i-1] != 1:
            seq.append(i)
            new_start = i
            dfs(new_start, end, visited, seq, max_length)
            seq.pop()


N, M = map(int, input().split(' '))
visit = [0] * N
sequence = []
dfs(1, N+1, visit, sequence, M)
