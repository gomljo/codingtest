from itertools import product
from collections import defaultdict
from bisect import bisect_left

"""
이 문제는 검색 조건이 정해져 있다.
모든 조건은 '-'를 포함하여 4개, 3개, 3개, 3개로 product 함수를 이용하여 구한 경우의 수는 최대 108가지로 제한된다.
경우의 수 마다 해시 맵을 구성하여 해당하는 경우의 점수들을 저장하는 방식을 택할 수 있다.

가장 단순한 방법은 중첩된 반복문의 사용으로 조건을 모두 비교하는 것이지만 
info 배열은 최대 5만, query 배열은 최대 10만으로 중첩된 반복문을 사용할 경우 시간 초과가 발생한다.

주의해야할 사항이 하나 더 있다.
검색 후 점수 비교에 대한 것이다.
일반적인 반복문을 통한 탐색의 경우 시간 초과가 발생하며 효율적인 목표 값 탐색을 진행할 수 있는
이진 탐색 방식으로 점수를 비교하여야 문제가 발생하지 않는다.
"""
def solution(info, query):
    answer = []
    case_dict = defaultdict(list)

    for i in info:  # 50000
        items = i.split()
        condition, score = items[:-1], int(items[-1])
        conditions = []

        # 조건마다 '-'를 경우의 수에 포함하기
        # ex) java backend senior pizza의 경우 [java, -] X [backend, -] X [senior, -] X [pizza, -] => 16가지의 경우
        for c in condition:  # 4
            conditions.append([c, '-'])

        # '-'를 포함하는 모든 경우의 수 구하기
        info_cases = list(product(*conditions))

        # 구한 경우들에 대해 값을 저장
        # 딕셔너리의 value를 리스트로 지정한 것은 중복된 info가 존재할 경우를 대비하기 위함이다.
        for case in info_cases:  # 16
            case_dict[case].append(score)
    # 이진 탐색을 진행하기 위해 값들을 정렬한다.
    for value in case_dict.values():
        value.sort()

    # 쿼리들에 대해 해당하는 경우의 점수들을 구하여 이진 탐색을 수행한다.
    # 이진 탐색 결과는 score 보다 작지만 가장 가까운 수의 인덱스가 반환된다.
    # 따라서 총 점수의 갯수 - 이진 탐색 결과 인덱스가 만족하는 쿼리의 갯수가 된다.
    for q in query:
        q = q.replace('and', ' ')
        items = q.split()
        condition, score = tuple(items[:-1]), int(items[-1])
        idx = bisect_left(case_dict[condition], score)
        cnt = len(case_dict[condition]) - idx
        answer.append(cnt)
    return answer