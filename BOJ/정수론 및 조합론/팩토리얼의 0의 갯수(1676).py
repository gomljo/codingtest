import re
N = int(input())
five_list = []
two_list = []
ten_list = []
for i in range(N+1):

    if list(str(i))[-1] in ['2', '4', '6', '8']:
        two_list.append(i)
    if list(str(i))[-1] in ['5']:
        five_list.append(i)
    if i % 10 == 0 and i != 0:
        ten_list.append(i)

if five_list and two_list:
    num = 1
    num_of_pair = min(len(five_list), len(two_list))
    for two, five in zip(two_list[:num_of_pair], five_list[:num_of_pair]):
        num *= two * five
    for ten in ten_list:
        num *= ten
    num_string = str(num)
    num_string = re.sub('[1-9]', '*', num_string)
    num_string = num_string.split('*')[-1]
    print(len(num_string))
else:
    print(0)
