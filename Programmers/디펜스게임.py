from collections import Counter


def recursion(seq, s, e, k, n):
    mid = (s + e) // 2
    print('in', s, mid, e)
    left = seq[:mid]
    left.sort(reverse=True)
    if sum(left[k:]) >= n:
        part = seq[:mid + 1]
        part.sort(reverse=True)
        if sum(part[k:]) >= n:
            return s
        s = recursion(seq, s, mid, k, n)
    else:
        s = recursion(seq, mid, e, k, n)
    return s


def solution(n, k, enemy):
    answer = 0
    if len(enemy) <= k:
        return len(enemy)
    # 최적화와 메모리 문제로 이진 탐색으로 진행
    # 검사 기준은 큰 수를 내림차순으로 정렬하여 무적권의 갯수를 초과하는지 검사
    #
    # 적의 공격 시퀀스의 길이의 1/2 지점을 기준으로 왼쪽을 검사
    # 중앙 기준 왼쪽이 무적권을 이용하여 클리어할 수 없다면 왼쪽의 길이의 1/2 지점의 왼쪽을 검사
    # 중앙 기준 왼쪽이 무적권을 이용하여 클리어할 수 있다면 오른쪽 길이의 1/2 지점의 왼쪽을 검사

    answer = recursion(enemy, 0, len(enemy), k, n)

    return answer


n = 7
k = 1
enemy = [7,3,4,5,3,3,1]
solution(n, k, enemy)