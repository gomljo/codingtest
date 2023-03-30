def solution(number):
    answer = 0
    visited = [0] * len(number)
    trio = []

    def dfs(start, numbers):
        nonlocal answer
        if len(trio) == 3:
            if sum(trio) == 0:
                answer += 1
                return

        for i in range(start, len(numbers)):

            if visited[i] != 1:
                visited[i] = 1
                trio.append(numbers[i])
                start += 1
                dfs(start, numbers)
                trio.pop()
                visited[i] = 0

    dfs(0, trio)

    return answer
