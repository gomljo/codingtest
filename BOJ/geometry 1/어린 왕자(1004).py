# import math
#
# N = int(input())
#
# expected_answer = []
# answer = []
# for i in range(N):
#     expected_answer.append(int(input()))
#
# for i in range(N):
#
#     s_x, s_y, t_x, t_y = map(int, input().split(' '))
#     # 시작 점을 포함하는 행성의 리스트
#     s_planets = []
#     # 도착 점을 포함하는 행성의 리스트
#     t_planets = []
#
#     num_of_planet = int(input())
#
#     for j in range(num_of_planet):
#
#         # 각 행성의 중심 x 좌표, 중심 y 좌표, 반지름
#         p_x, p_y, p_r = map(int, input().split(' '))
#         # 시작점과 도착점이 어떤 행성에 포함되는 지 알아보기 위한 계산
#         s_dist = math.sqrt((s_x-p_x)**2+(s_y-p_y)**2)
#         t_dist = math.sqrt((t_x-p_x)**2+(t_y-p_y)**2)
#
#         # 시작 점을 포함하는 행성이 있다면 추가
#         if s_dist < p_r:
#             s_planets.append([s_dist, p_x, p_y, p_r])
#
#         # 도착 점을 포함하는 행성이 있다면 추가
#         if t_dist < p_r:
#             t_planets.append([t_dist, p_x, p_y, p_r])
#     print(len(s_planets)+len(t_planets))
#     answer.append(len(s_planets)+len(t_planets))
#
#
# def validate_answer(answer, expected_answer):
#     for test_case_idx, (a, ea) in enumerate(zip(answer, expected_answer)):
#         print('테스트 검증')
#
#         print('{}번 째 테스트 케이스'.format(test_case_idx+1))
#
#         print('예상되는 어린 왕자가 거치는 최소 행성계 진입/이탈 횟수: {}'.format(expected_answer[test_case_idx]))
#         print('어린 왕자가 거치는 최소 행성계 진입/이탈 횟수: {}'.format(answer[test_case_idx]))
#         if expected_answer[test_case_idx] == answer[test_case_idx]:
#             print('맞혔습니다')
import math

# 테스트 케이스의 수를 입력
N = int(input())

# 행성 계 이탈/진입 횟수를 저장하기 위한 배열 선언
answer = []

# 테스트 케이스의 수 만큼 반복
for i in range(N):
    s_x, s_y, t_x, t_y = map(int, input().split(' '))

    # 시작 점을 포함하는 행성의 리스트
    s_planets = []
    # 도착 점을 포함하는 행성의 리스트
    t_planets = []

    # 행성 계의 수를 입력
    num_of_planet = int(input())

    # 행성 계의 수 만큼 반복
    for j in range(num_of_planet):

        # 각 행성의 중심 x 좌표, 중심 y 좌표, 반지름
        p_x, p_y, p_r = map(int, input().split(' '))

        # 시작점과 도착점이 어떤 행성에 포함되는 지 알아보기 위한 계산
        s_dist = math.sqrt((s_x-p_x)**2+(s_y-p_y)**2)
        t_dist = math.sqrt((t_x-p_x)**2+(t_y-p_y)**2)

        # 맞는데 왜 틀렸지 포인트
        # 두 행성을 모두 포함하는 행성계가 존재할 수도 있기 떄문에 둘 다 포함된다면
        # 행성 포함 리스트에서 제거해야한다.
        if s_dist < p_r and t_dist < p_r:
            continue

        # 시작 점을 포함하는 행성이 있다면 추가
        if s_dist < p_r:
            s_planets.append([s_dist, p_x, p_y, p_r])

        # 도착 점을 포함하는 행성이 있다면 추가
        if t_dist < p_r:
            t_planets.append([t_dist, p_x, p_y, p_r])

    # 행성계를 진입/이탈하는 횟수는 두 점을 포함하는 원의 수와 같다.
    answer.append(str(len(s_planets)+len(t_planets)))

print('\n'.join(answer))
