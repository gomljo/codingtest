from math import comb

N, M = map(int, input().split(' '))

M_cnt_five = []
N_cnt_five = []
M_cnt_two = []
N_cnt_two = []

exponential = 1
count = 0

if M==N:
    print(count)
elif M==0:
    print(count)
else:

    while (N // (5 ** exponential)) != 0:
        N_cnt_five.append(N // (5**exponential))
        exponential += 1
    exponential = 1

    while (N // 2 ** exponential) != 0:
        N_cnt_two.append(N // (2 ** exponential))
        exponential += 1
    exponential = 1
    n_k = N - M
    while (n_k // 5 ** exponential) != 0:
        N_cnt_five[exponential-1] -= n_k // (5 ** exponential)
        exponential += 1
    exponential = 1

    while (n_k // 2 ** exponential) != 0:
        N_cnt_two[exponential-1] -= n_k // (2 ** exponential)
        exponential += 1
    exponential = 1

    while (M // 5 ** exponential) != 0:
        N_cnt_five[exponential-1] -= (M // (5**exponential))
        exponential += 1
    exponential = 1

    while (M // 2 ** exponential) !=0:
        N_cnt_two[exponential - 1] -= M // (2 ** exponential)
        exponential+=1
    exponential=1
    two_total_cnt = sum(N_cnt_two)
    five_total_cnt = sum(N_cnt_five)
    print(min(two_total_cnt, five_total_cnt))

    # if N_cnt_two >= M_cnt_two:
    #     print((N_cnt_five - M_cnt_five))
    # else:
    #     print((N_cnt_five - M_cnt_five) - (M_cnt_five - N_cnt_five))



# if M == 0 or M == N:
#     print(0)
# else:
#     numerator_five_list = []
#     numerator_two_list = []
#     numerator_ten_list = []
#
#     denominator_five_list = []
#     denominator_two_list = []
#     denominator_ten_list = []
#
#     for i in range(N, N - M + 1, -1):
#
#         if list(str(i))[-1] in ['2', '4', '6', '8']:
#             numerator_two_list.append(i)
#         if list(str(i))[-1] in ['5']:
#             numerator_five_list.append(i)
#         if i % 10 == 0 and i != 0:
#             numerator_ten_list.append(i)
#     num_of_pair = min(len(numerator_five_list), len(numerator_two_list))
#     numerator = 1
#
#     for two in denominator_two_list:
#         numerator *= two
#     for five in denominator_five_list:
#         numerator *= five
#     for ten in numerator_ten_list:
#         numerator *= ten
#
#     for j in range(1, M+1):
#
#         if list(str(j))[-1] in ['2', '4', '6', '8']:
#             denominator_two_list.append(j)
#         if list(str(j))[-1] in ['5']:
#             denominator_five_list.append(j)
#         if j % 10 == 0 and j != 0:
#             denominator_ten_list.append(j)
#     denominator = 1
#     num_of_pair = min(len(denominator_five_list), len(denominator_two_list))
#
#     for two in denominator_two_list:
#         denominator *= two
#     for five in denominator_five_list:
#         denominator *= five
#     for ten in denominator_ten_list:
#         denominator *= ten
#
#     num = int(numerator / denominator)

# num_string = str(num)

# num_string = re.sub('[1-9]', '*', num_string)
# num_string = num_string.split('*')[-1]
# print(len(num_string))

