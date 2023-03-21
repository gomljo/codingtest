from collections import defaultdict

x_coords = defaultdict(int)
y_coords = defaultdict(int)


for _ in range(3):
    x, y = map(int, input().split(' '))
    x_coords[x] += 1
    y_coords[y] += 1

x, y = 0, 0
for x_key, y_key in zip(x_coords.keys(), y_coords.keys()):

    if x_coords[x_key] == 1:
        x = x_key

    if y_coords[y_key] == 1:
        y = y_key

print(x, y)