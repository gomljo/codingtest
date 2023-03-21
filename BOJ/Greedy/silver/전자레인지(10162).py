n = int(input())

num_of_push = ['0', '0', '0']
A = 300
B = 60
C = 10
buttons = [A, B, C]
for idx, button in enumerate(buttons):
    if n // button > 0:
        num_of_push[idx] = str(n // button)
        n = n % button
if n != 0:
    print(-1)
else:
    print(' '.join(num_of_push))