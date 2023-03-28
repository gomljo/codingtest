import math


def calcPoint(m, cueBall, objectBall, flag):
    if flag == "L" or flag == "R":
        numerator = (cueBall[0] - m) * objectBall[1] + (objectBall[0] - m) * cueBall[1]
        denumerator = (cueBall[0] - m) + (objectBall[0] - m)
        return [m, numerator / denumerator]
    else:
        numerator = (cueBall[1] - m) * objectBall[0] + (objectBall[1] - m) * cueBall[0]
        denumerator = (cueBall[1] - m) + (objectBall[1] - m)
        return [numerator / denumerator, m]


def solution(m, n, startX, startY, balls):
    answer = []
    start = [startX, startY]
    for ball in balls:
        points = []
        vector = [ball[0] - start[0], ball[1] - start[1]]
        # 한쪽 면으로 원 쿠션이 성립하지 않을 경우
        if vector[0] == 0 and vector[1] < 0:
            # left, right, bottom
            constant = [[0, "L"], [m, "R"], [0, "B"]]
            for c in constant:
                points.append(calcPoint(c[0], start, ball, c[1]))

        elif vector[0] == 0 and vector[1] > 0:
            # left, right, top
            constant = [[0, "L"], [m, "R"], [n, "T"]]
            for c in constant:
                points.append(calcPoint(c[0], start, ball, c[1]))
        elif vector[0] < 0 and vector[1] == 0:
            # right, top, bottom
            constant = [[m, "R"], [n, "T"], [0, "B"]]
            for c in constant:
                points.append(calcPoint(c[0], start, ball, c[1]))
        elif vector[0] > 0 and vector[1] == 0:
            # left, top, bottom
            constant = [[0, "L"], [n, "T"], [0, "B"]]
            for c in constant:
                points.append(calcPoint(c[0], start, ball, c[1]))
        # 모든 면에 원 쿠션이 성립되는 경우
        else:
            # left, right, top, bottom
            constant = [[0, "L"], [m, "R"], [n, "T"], [0, "B"]]
            for c in constant:
                points.append(calcPoint(c[0], start, ball, c[1]))
        minDist = math.inf
        print(points)
        for p in points:
            fromCue = math.sqrt(math.pow(start[0] - p[0], 2) + math.pow(start[1] - p[1], 2))
            fromObject = math.sqrt(math.pow(ball[0] - p[0], 2) + math.pow(ball[1] - p[1], 2))
            dist = fromCue + fromObject
            if minDist > dist:
                minDist = dist
        print(minDist**2)
        answer.append(round(minDist ** 2))
    return answer

solution(10,10,2,7,[[3, 7], [2, 7], [7, 2]])