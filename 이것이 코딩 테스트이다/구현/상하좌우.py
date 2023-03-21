
def is_over(changed_pos):
    for pos in range(len(changed_pos)):
        if changed_pos[pos] <= 0 or changed_pos[pos] > N:
            return True
    return False


def change_pos(cur_pos, moved_pos):
    return [cur_pos[0] + moved_pos[0], cur_pos[1]+moved_pos[1]]


def print_result(cur_pos):
    print(cur_pos[0], cur_pos[1])


N = int(input())
path = input().split()

move = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}
current_pos = [1, 1]

for moving in path:
    pos_changed = change_pos(current_pos, move[moving])
    if not is_over(pos_changed):
        current_pos = pos_changed

print_result(current_pos)