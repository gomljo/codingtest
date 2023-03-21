# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# ***
# * *
# ***
# -> 크기 3의 패턴은 가운데 3/3(=1) X 3/3(=1) 정사각형을 크기 3/3(=1)의 패턴으로 둘러싼 형태이다.
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
# 즉 N=9인 경우, 가운데 9/3(=3) X 9/3(=3) 정사각형을 크기 9/3(=3)의 패턴으로 둘러싼 형태이다.

def print_stars(pattern, current, trial):
    new_pattern = [[],[],[]]
    if current == trial:
        return '\n'.join(pattern[0]) + '\n' + '\n'.join(pattern[1]) + '\n' + '\n'.join(pattern[2])
    for i in range(3):
        for j in range(3):
            for p in pattern[j]:
                if i == 1:
                    new_pattern[i].append(str(p) + ' ' * current + str(p))
                else:

                    new_pattern[i].append(str(p) * 3)
    current *= 3
    return print_stars(new_pattern, current, trial)


n = int(input())

pattern_3X3 = [["***"], ["* *"], ["***"]]

answer = print_stars(pattern_3X3, 3, n)
print(answer)