N = int(input())
ability = []
visited = [0] * N

s_total = set([x for x in range(N)])
s_start = list()
s_link = set()

for i in range(N):
    ability.append(list(map(int, input().split(' '))))


def calc_ability(team, pair, visit, sum):

    if len(pair) == 2:
        print('pair', pair)
        print('sum', ability[pair[0]][pair[1]] + ability[pair[1]][pair[0]])
        return ability[pair[0]][pair[1]] + ability[pair[1]][pair[0]]

    for j in range(len(team)):

        if visit[j] != 1:
            visit[j] = 1
            pair.append(team[j])
            sum += calc_ability(team, pair, visit, sum)
            pair.pop()
            visit[j] = 0
    return sum

def backtracking(start, link, visit, condition):
    if len(start) == condition:
        start = set(start)
        link = s_total.difference(start)
        print(start)
        print(link)
        visit_team = [0] * condition
        pair_start = []
        pair_link = []
        ability_start = 0
        ability_link = 0
        ability_start = calc_ability(list(start), pair_start, visit_team, ability_start)
        ability_link = calc_ability(list(link), pair_link, visit_team, ability_link)
        print(ability_start)
        print(ability_link)
        return
        # return ability_sum

    for i in range(N):
        if visit[i] != 1:
            visit[i] = 1
            start.append(i)
            backtracking(start, link, visit, condition)
            start.pop()
            visit[i] = 0
    return

backtracking(s_start, s_link, visited, N//2)