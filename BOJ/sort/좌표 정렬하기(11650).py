n = int(input())
coords = [list(map(int, input().split(' '))) for _ in range(n)]

sorted_coords = sorted(coords, key=lambda x:(x[0], x[1]))
for coord in sorted_coords:
    print(coord[0], coord[1])