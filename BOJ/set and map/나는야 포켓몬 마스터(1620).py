N, M = map(int, input().split(' '))

pocket_name = dict()
pocket_id = dict()

for i in range(N):
    name = input()
    pocket_name[name] = i+1
    pocket_id[i+1] = name

queries = []

for j in range(M):
    queries.append(input())

for query in queries:
    if query in pocket_name.keys():
        print(pocket_name[query])
    else:
        print(pocket_id[int(query)])