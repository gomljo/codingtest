import math
row, col = map(int, input().split(' '))
board = [[1 if x == 'B' else 0 for x in list(input())] for _ in range(row)]

pattern1 = [[1,0]*4, [0,1]*4] * 4
pattern2 = [[0,1]*4, [1,0]*4] * 4

want_size = 8

row_start = 0
row_end = 8
col_start = 0
col_end = 8

new_board = []
min_change = math.inf
row_range = row-want_size+1
col_range = col-want_size+1

for r in range(row-want_size+1):
    new_board = board[row_start+r: row_end+r]
    for c in range(col-want_size+1):
        change = 0
        start_b = 0
        start_w = 0
        for row, p1_row, p2_row in zip(new_board, pattern1, pattern2):
            row = row[col_start+c: col_end+c]
            start_b += sum([1 if abs(r-p) != 0 else 0 for (r, p) in zip(row, p1_row)])
            start_w += sum([1 if abs(r-p) != 0 else 0 for (r, p) in zip(row, p2_row)])
        change = min(start_b, start_w)
        min_change = min(min_change, change)
print(min_change)
# if row > want_size and col > want_size:
#     for r in range(row-want_size+1):
#         print(row_start+r, row_end+r)
#         new_board = board[row_start+r: row_end+r]
#         print(new_board)
#         for c in range(col-want_size+1):
#             change = 0
#             start_b = 0
#             start_w = 0
#             for row, p1_row, p2_row in zip(new_board, pattern1, pattern2):
#                 row = row[col_start+c: col_end+c]
#                 start_b += sum([1 if abs(r-p) != 0 else 0 for (r, p) in zip(row, p1_row)])
#                 start_w += sum([1 if abs(r-p) != 0 else 0 for (r, p) in zip(row, p2_row)])
#             change = min(start_b, start_w)
#             print(change)
#             min_change = min(min_change, change)
#
# elif row > want_size:
#     for r in range(row - want_size+1):
#         change = 0
#         start_b = 0
#         start_w = 0
#         new_board = board[row_start + r: row_end + r]
#         for row, p1_row, p2_row in zip(new_board, pattern1, pattern2):
#             row = row[col_start: col_end]
#             start_b += sum([1 if abs(r - p) != 0 else 0 for (r, p) in zip(row, p1_row)])
#             start_w += sum([1 if abs(r - p) != 0 else 0 for (r, p) in zip(row, p2_row)])
#         change = min(start_b, start_w)
#         print(change)
#         min_change = min(min_change, change)
# elif col > want_size:
#     for c in range(col - want_size+1):
#         change = 0
#         new_board = board
#         start_b = 0
#         start_w = 0
#         for row, p1_row, p2_row in zip(new_board, pattern1, pattern2):
#             row = row[col_start + c: col_end + c]
#             start_b += sum([1 if abs(r - p) != 0 else 0 for (r, p) in zip(row, p1_row)])
#             start_w += sum([1 if abs(r - p) != 0 else 0 for (r, p) in zip(row, p2_row)])
#         change = min(start_b, start_w)
#         print(change)
#         min_change = min(min_change, change)
#
# elif row == want_size and col == want_size:
#     change = 0
#     new_board = board
#     start_b = 0
#     start_w = 0
#     for row, p1_row, p2_row in zip(new_board, pattern1, pattern2):
#         row = row[col_start: col_end]
#         start_b += sum([1 if abs(r - p) != 0 else 0 for (r, p) in zip(row, p1_row)])
#         start_w += sum([1 if abs(r - p) != 0 else 0 for (r, p) in zip(row, p2_row)])
#     change = min(start_b, start_w)
#     print(change)
#     min_change = min(min_change, change)

