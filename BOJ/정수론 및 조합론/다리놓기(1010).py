from math import comb
N = int(input())
numbers = []
for _ in range(N):
    A, B = map(int, input().split(' '))
    numbers.append([A, B])

for number in numbers:
    A, B = min(number), max(number)
    print(comb(B,A))
# for number in numbers:
#     A, B = min(number), max(number)
#     total_possibles = 0
#     result = list()
#     for i in range(A):
#         order = (i+1)
#         reminder = B - A + (2-order)
#         nums = [1] * (A - 1)
#         nums.append(reminder)
#
#         head = nums[:A-order]
#
#         mid = nums[A-order: A-order+2]
#         tail = nums[A-order+2:]
#         rest = sum(head) + sum(tail)
#         new_nums = []
#
#         if len(mid) == 1:
#             result.append(nums)
#             continue
#         for add_second_term in range(0, reminder):
#             new_second_term = mid[1] + add_second_term
#             for add_first_term in range(1, reminder):
#                 new_first_term = mid[0] + add_first_term
#                 new_sum = new_first_term + new_second_term
#                 if rest + new_sum == B:
#
#                     if tail:
#                         new_nums = nums[:A - order] + [new_first_term, new_second_term] + tail
#                     else:
#                         new_nums = nums[:A - order] + [new_first_term, new_second_term]
#
#                     new_nums.sort()
#                     if new_nums not in result:
#                         cnt_res = Counter(new_nums)
#                         repeats = factorial(A)
#                         possibles = 1
#                         for unique, cnt in cnt_res.items():
#                             repeats /= factorial(cnt)
#                             if unique == 1:
#                                 possibles *= cnt
#                             else:
#                                 possibles *= unique
#                         total_possibles += repeats * possibles
#                         result.append(new_nums)
#     print(total_possibles)
