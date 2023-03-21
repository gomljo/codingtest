expression = input()
tokens = expression.split('-')

total_sum = 0
for idx, token in enumerate(tokens):
    temp_sum = 0
    for num in token.split('+'):
        temp_sum += int(num)
    if idx == 0:
        total_sum += temp_sum
    else:
        total_sum -= temp_sum
print(total_sum)