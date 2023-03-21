import sys

num_of_data, interval = map(int, input().split(' '))

data = [int(x) for x in sys.stdin.readline().split(' ')]

initial_sum = 0

for i in range(interval):
    initial_sum += data[i]
max_val = initial_sum

for j in range(interval, num_of_data):

    initial_sum -= data[j-interval]
    initial_sum += data[j]
    if initial_sum > max_val:
        max_val = initial_sum
print(max_val)