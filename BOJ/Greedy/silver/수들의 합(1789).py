
n = int(input())

range_sum = 0
last_number = 0
number = 0
while True:
    number += 1
    range_sum = (number*(number+1))//2
    if range_sum > n:
        number -= 1
        break
print(number)