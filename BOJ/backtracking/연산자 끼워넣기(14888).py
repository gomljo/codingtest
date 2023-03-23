# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
# 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다.
# 이때, 주어진 수의 순서를 바꾸면 안 된다.

# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
# 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
# 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.

def calculation(operand1, operand2, operator):

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == 'x':
        return operand1 * operand2
    else:
        if operand1 < 0:
            temp = abs(operand1) // operand2
            return temp * -1
        else:
            return operand1 // operand2


def backtracking(res, res_list, used, operators, numbers):
    if len(res) == len(operators):
        # print(res)
        # res_list.append(res)
        return res

    for i in range(len(operators)):
        if used[i] != 1:
            used[i] = 1
            op = operator[i]
            # res.append(calculation(numbers[i], numbers[i+1], op))
            res.append(op)
            new_res = backtracking(res, res_list, used, operators, numbers)
            # if len(res) == len(operators):
            if not new_res and len(new_res) == len(operators):
                res_list.append(new_res)
            # print(new_res)
            # print(res_list)
            # if not res:
            res.pop()
            # res_list.append(res)
            used[i] = 0
    return res_list


operator = []
# 수열 내 숫자의 갯수
num_of_numbers = int(input())

# 수열
sequence = list(map(int, input().split(' ')))

# 연산자의 갯수들을
num_of_operators = list(map(int, input().split(' ')))

for idx, op_num in enumerate(num_of_operators):

    if idx == 0:
        operator.extend(['+'] * op_num)
    elif idx == 1:
        operator.extend(['-'] * op_num)
    elif idx == 2:
        operator.extend(['x'] * op_num)
    else:
        operator.extend(['/'] * op_num)
result = []
results = []
print(operator)
op_used = [0] * sum(num_of_operators)
results = backtracking(result, results, op_used, operator, sequence)
print(results)
