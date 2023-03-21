def solution(number, k):
    answer = ''
    number = list(number)
    wanted_digit = len(number) - k
    deleted = 0
    while wanted_digit != 0:

        pick_range = len(number) - wanted_digit + 1
        # pick = number[:pick_range]
        max_val = max(number)
        max_pos = number.index(max_val)
        deleted += max_pos
        answer += number[max_pos]
        number = number[max_pos + 1:]
        wanted_digit -= 1




    return answer

number = "4177252841"
k = 9
ans = solution(number, k)
print(ans)
print(len(ans))
print(len(number)-k)
