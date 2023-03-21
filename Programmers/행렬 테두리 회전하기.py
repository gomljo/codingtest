from collections import deque


def make_matrix(row, column):
    matrix = []
    for r in range(row):
        row_mat = []
        for c in range(1, column + 1):
            row_mat.append(r * column + c)
        matrix.append(row_mat)
    return matrix


def find_idx(coordinate):
    x1, y1, x2, y2 = coordinate[0], coordinate[1], coordinate[2], coordinate[3]
    # 중복된 좌표 제거를 위해 set 자료형으로 선언
    idxs = list()
    # top
    for t in range(y1, y2 + 1):
        if (x1, t) not in idxs:
            idxs.append((x1, t))
    # right
    for r in range(x1, x2 + 1):
        if (r, y2) not in idxs:
            idxs.append((r, y2))
    # bottom
    for b in range(y2, y1 - 1, -1):
        if (x2, b) not in idxs:
            idxs.append((x2, b))
    # left
    for l in range(x2, x1 - 1, -1):
        if (l, y1) not in idxs:
            idxs.append((l, y1))
    print(idxs)
    return idxs


def clockwise_transform(matrix, coordinates):
    # queue를 이용하여 순서 바꾸기
    queue = deque()
    for coordinate in coordinates:
        num = matrix[coordinate[0] - 1][coordinate[1] - 1]
        queue.append(num)
    min_val = min(queue)
    first_element = queue.popleft()
    queue.append(first_element)

    for coordinate in coordinates:
        matrix[coordinate[0] - 1][coordinate[1] - 1] = queue.popleft()

    return matrix, min_val


def solution(rows, columns, queries):
    answer = []
    matrix = make_matrix(rows, columns)
    for query in queries:
        target_index = find_idx(query)
        matrix, min_val = clockwise_transform(matrix, target_index)
        print(min_val)
        # answer.append(min_val)

    return answer


rows = [6, 3, 100]
columns = [6, 3, 97]
queries = [[[2,2,5,4],[3,3,6,6],[5,1,6,3]], [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]], [[1,1,100,97]]]

for r, c, q in zip(rows, columns, queries):
    ans = solution(r,c,q)
