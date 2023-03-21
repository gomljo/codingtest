from bisect import bisect_left


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def get_number(n, k, cases, numbers):
    possible_cases = factorial(n)
    interval = factorial(n - 1)
    interval_list = [i * interval for i in range(1, n)]
    interval_list.append(possible_cases)

    if n > 2:
        idx = bisect_left(interval_list, k)

        numbers.append(cases.pop(idx))
        if k % interval == 0:
            k = (k-1) % interval
            k+=1
        else:
            k = k % interval
        return get_number(n - 1, k, cases, numbers)

    elif n==1:
        return [1]

    else:
        k = k % 2
        if k < 1:
            numbers.extend([cases[1], cases[0]])
        else:
            numbers.extend([cases[0], cases[1]])
        return numbers


def solution(n, k):
    answer = []
    cases = [i for i in range(1, n + 1)]
    answer = get_number(n, k, cases, answer)
    return answer


n = 20
k = factorial(20)-1
print(k)

print(solution(n, k))