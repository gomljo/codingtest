pos = input()
row = int(pos[1])
col = ord(pos[0]) - ord('a') + 1
# print(row, col)
cnt = 0
for direc in range(2):

    for i in [-2, 2]:

        for j in [-1, 1]:
            row_ = 0
            col_ = 0
            if direc == 0:
                row_ = row + i
                col_ = col + j
                if 0 < row_ < 7 and 0 < col_ < 7:
                    cnt += 1
            else:
                row_ = row + j
                col_ = col + i
                if 0 < row_ < 7 and 0 < col_ < 7:
                    cnt += 1
print(cnt)

