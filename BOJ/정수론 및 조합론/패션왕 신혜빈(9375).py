from collections import defaultdict

num_of_test = int(input())
total = []
for test_num in range(num_of_test):

    num_of_cloth = int(input())
    closet = defaultdict(int)

    for i in range(num_of_cloth):
        cloth_name, category = input().split(' ')
        closet[category] += 1
    # 뽑은 카테고리의 옷들을 착용하는 모든 경우의 수 계산
    temp = 0
    possible = 1
    for category in closet:
        possible *= (closet[category] + 1)
    temp += possible
    total.append(str(temp-1))
# 결과 출력
print('\n'.join(total))