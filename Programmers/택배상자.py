def solution(order):
    temp = []
    i = 1
    now = 0

    while i != len(order) + 1:
        temp.append(i)
        print('append ', temp)
        while temp[-1] == order[now]:
            print('in while ', temp)
            now += 1
            temp.pop()

            if len(temp) == 0:
                break
        i += 1

    return now


order = [4,3,1,2,5]
res = solution(order)
print(res)