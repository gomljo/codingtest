# direction = {0: 3, 1: 0, 2: 1, 3: 2}
direction = [0,1,2,3]
moving = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}


def change_90_counter_clockwise_direction(cur_direc):

    idx = direction.index(cur_direc)
    return direction[idx - 1]


def change_180_degree_direction(cur_direc):

    idx = direction.index(cur_direc)
    return direction[idx - 2]


def move(cur_pos, next_moving):

    return [cur_pos[0] + next_moving[0], cur_pos[1] + next_moving[1]]


def stage2(cur_pos, cur_direc, game_map):

    next_direc = change_90_counter_clockwise_direction(cur_direc)
    next_move = moving[next_direc]
    next_pos = move(cur_pos, next_move)

    if next_pos != 1:
        change_map(cur_pos, game_map)
        return next_pos


def is_all_visited(cur_pos):
    for m in moving.items():
        next_pos = move(cur_pos, m)
        if next_pos != 1:
            return False
    return True


def move_behind(cur_pos, cur_direc):
    behind_direc = change_180_degree_direction(cur_direc)
    behind_move = moving[behind_direc]
    behind_pos = move(cur_pos, behind_move)
    return behind_pos


def is_sea_on_behind(behind_pos):

    if behind_pos == 1:
        return True

    return False


def stage3(cur_pos, cur_direction):

    if is_all_visited(cur_pos):
        behind_pos = move_behind(cur_pos, cur_direction)
        if not is_sea_on_behind(behind_pos):
            return behind_pos
    return cur_pos


def change_map(cur_pos, game_map):

    game_map[cur_pos[0]][cur_pos[1]] = 1


def solution():
    N, M = map(int, input().split())

    row, col, direc = map(int, input().split())
    current_position = [row, col]
    game_map = [[int(i) for i in input().split()] for _ in range(N)]

    current_position = stage2(current_position, direc, game_map)

