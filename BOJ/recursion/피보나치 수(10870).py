def fibonacci(first_term, second_term, current_n, target_n):
    third_term = first_term + second_term
    if target_n == 0:
        return first_term
    if target_n == 1:
        return second_term

    if current_n == target_n:
        return third_term
    first_term = second_term
    second_term = third_term
    current_n += 1
    return fibonacci(first_term, second_term,current_n, target_n)


def fibonacci_2(first_term, second_term, current, target):
    if target == 0:
        return first_term
    if target == 1:
        return second_term
    third_term = 0
    while current <= target:
        third_term = second_term + first_term
        first_term = second_term
        second_term = third_term
        current += 1

    return third_term


number = int(input())

F_n_1 = 1
F_n_2 = 0
print(fibonacci(F_n_2, F_n_1, 2, number))
print(fibonacci_2(F_n_2, F_n_1, 2, number))