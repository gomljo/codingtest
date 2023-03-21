import sys
input = sys.stdin.readline

arr_size, num_of_queries = map(int, input().split(' '))

arr = []

for i in range(arr_size):
    arr.append([int(x) for x in input().split(' ')])

prefix_arr = [[0] * (arr_size+1)]

for j in range(arr_size):
    prefix_sum = 0
    temp_prefix = prefix_arr[j][:]
    for k in range(arr_size):
        prefix_sum += arr[j][k]
        temp_prefix[k+1] += prefix_sum
    prefix_arr.append(temp_prefix[:])

for q in range(num_of_queries):
    s_x, s_y, e_x, e_y = map(int, input().split(' '))
    interval_sum = prefix_arr[e_x][e_y] - prefix_arr[s_x-1][e_y] - prefix_arr[e_x][s_y-1] + prefix_arr[s_x-1][s_y-1]
    print(interval_sum)