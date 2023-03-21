n = int(input())
infos = []
for i in range(n):
    age, name = input().split(' ')
    infos.append([int(age), i, name])

infos_sorted = sorted(infos, key=lambda x: (x[0], x[1]))
for info in infos_sorted:
    print(info[0], info[2])