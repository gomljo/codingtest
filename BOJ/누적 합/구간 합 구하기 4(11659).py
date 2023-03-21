num_of_data, length = map(int, input().split(' '))
prefix = [0]
sum = 0

data = [int(x) for x in input().split(' ')]
for i in range(num_of_data):
    sum += data[i]
    prefix.append(sum)

answer = []
for q in range(length):
    left, right = map(int, input().split(' '))
    answer.append(str(prefix[right] - prefix[left-1]))

print('\n'.join(answer))
