def solution(storey):
    answer = 0
    length = len(list(str(storey)))
    base = 0
    cnt = 0
    while cnt < length:
        if storey > 0:
            elements = str(storey)
        else:
            elements = str(abs(storey))
        first = int(elements[0])
        base = length - cnt - 1

        if base > 0:
            upper = (first + 1) * 10 ** base
            bottom = (first) * 10 ** base
        else:
            upper = 10
            bottom = 0
        # print('upper', upper)
        # print('bottom', bottom)

        if storey > 0:
            upper_diff = (storey - upper)
            bottom_diff = (storey - bottom)
        else:
            upper_diff = (upper + storey)
            bottom_diff = (bottom + storey)

        # print('upper_diff', upper_diff)
        # print('bottom_diff', bottom_diff)

        # absolute 함수는 순수 크기 비교를 위한 L1 norm
        # 비교 시에만 absolute 함수를 사용하는 것은 프로그램의 목표가 0에 가까워지는 것이므로
        # 음수인 상태도 포함되기 때문이다.

        if abs(upper_diff) < abs(bottom_diff):
            storey = upper_diff
            answer += first + 1
        else:
            storey = bottom_diff
            answer += first
        cnt += 1

    return answer

def solution2(storey):
    answer = 0
    while storey != 0:
        n = storey % 10

        if n >= 6:
            storey += 10 - n
            answer += 10 - n

        elif n == 5 and (storey // 10) % 10 >= 5:
            storey += 10 - n
            answer += 10 - n

        else:
            answer += n
        storey = storey // 10


    return answer

storey = [16, 2554, 565787798]

for store in storey:
    res=solution(store)
    res2 = solution2(store)
    print(res, res2)