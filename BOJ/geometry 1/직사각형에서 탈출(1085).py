x, y, w, h = map(int, input().split(' '))

left_point_x = 0
left_point_y = 0

min_dist = min(min(x-left_point_x, w-x), min(y-left_point_y, h-y))
print(min_dist)