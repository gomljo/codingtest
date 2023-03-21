from collections import Counter


def dfs(points, length, board):
    moves = [[0, 1], [1, 0], [1, 1]]
    new_points = []
    is_border = False
    for point in points:
        for move in moves:
            new_x = point[0] + move[0]
            new_y = point[1] + move[1]
            if (new_x > len(board) - 1) or (new_y > len(board[0]) - 1):
                is_border |= True
                continue
            if board[new_x][new_y] == 0:
                return length
            else:
                new_points.append([new_x, new_y])

    if is_border:
        return length
    else:
        length += 1
        length = dfs(new_points, length, board)

    return length


def solution(board):
    answer = 0
    max_x = len(board)
    max_y = len(board[0])
    max_length = min(max_x, max_y)
    while max_length > 0:
        lengths = []
        new_board = []
        x_range = max_x - max_length + 1
        y_range = max_y - max_length + 1

        for x in range(x_range):

            new_board = board[x:x + max_length]
            for y in range(y_range):
                zero_cnt = 0
                for new_board_x in new_board:
                    if 0 in new_board_x[y:y + max_length]:
                        zero_cnt += 1
                if zero_cnt == 0:
                    lengths.append(max_length)
                    break
        if lengths:
            answer = lengths[0] ** 2
            break
        max_length -= 1

    # all_one_points = []
    # for x in range(len(board)):
    #     for y in range(len(board[0])):
    #         if board[x][y]==1:
    #             all_one_points.append([x,y])
    #             continue
    # temp_answer=0
    # for start_point in all_one_points:
    #     if board[start_point[0]][start_point[1]]!=0:
    #         temp_answer = dfs([start_point], length, board)
    #     answer = max(temp_answer, answer)

    return answer