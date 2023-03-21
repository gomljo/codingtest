num_of_trains = int(input())
customer = list(map(int, input().split(' ')))
max_trains = int(input())
num_of_mini_trains = 3

# 3대의 기차를 이용하여 max_trains 구간만큼 나누었을 때 가장 많은 승객을 태울 수 있도록 계산하라.
if max_trains < 2:
    customer.sort(reverse=True)
    print(sum(customer[:num_of_mini_trains]))

else:
    init_customer = 0

    for i in range(max_trains):
        init_customer += customer[i]

    prefix_customer = [init_customer]

    for j in range(max_trains, num_of_trains):
        init_customer -= customer[j - max_trains]
        init_customer += customer[j]
        prefix_customer.append(init_customer)

    max_customer_sum = 0
    pos = 0
    interval = max_trains * 2
    second_train_range = len(prefix_customer) // 3
    third_train_range = (len(prefix_customer) // 3) * 2
    while pos < second_train_range:
        first_train = prefix_customer[pos]
        second_train = max(prefix_customer[second_train_range+pos:third_train_range])
        third_train = max(prefix_customer[third_train_range+pos:])

        # print('1st: {}, 2nd: {}, 3rd: {}'.format(first_train, second_train, third_train))
        # print('1st: {}, 2nd: {}, 3rd: {}'.format(first_train, prefix_customer[second_train_range:], prefix_customer[third_train_range:]))

        total = first_train + second_train + third_train

        if max_customer_sum < total:
            max_customer_sum = total
        pos += 1

    print(max_customer_sum)
