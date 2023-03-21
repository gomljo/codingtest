from collections import deque
from itertools import islice
# version 1
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     second = 0
#     start_idx = 0
#     end_idx = 1
#     number_of_trucks = len(truck_weights)
#
#     on_bridge = []
#     start_time = 0
#     # cross_bridge = []
#     # 다리에 weight 무게 이하로 bridge_length만큼 올라갈 수 있는지 검사
#     while truck_weights:
#         truck_count = 0
#         for on_bridge_trucks in range(bridge_length):
#             if len(truck_weights) > on_bridge_trucks and sum(truck_weights[:on_bridge_trucks+1]) <= weight:
#                 start_time = second+on_bridge_trucks+1
#                 print(truck_weights[on_bridge_trucks])
#                 on_bridge.append((truck_weights[on_bridge_trucks], start_time+on_bridge_trucks+1))
#
#                 truck_count+=1
#                 print(truck_weights)
#             else:
#                 break
#         for _ in range(truck_count):
#             truck_weights.pop(0)
#             second+=start_time+2
#         start_idx = end_idx
#         print('on bridge', on_bridge, second)
#
#     return answer

# version 2
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     second=1
#     trucks=[]
#     on_bridge = []
#     on_bridge_second = []
#     on_bridge_weight = 0
#     new_second=0
#     while truck_weights:
#         idx = 0
#         # on_bridge_weight = 0
#         while idx < bridge_length:
#             print('idx: ', idx)
#             # if 0 < len(on_bridge) < bridge_length:
#             #     print(on_bridge[0], 'pop from on bridge')
#             #     print()
#             #     on_bridge_weight = on_bridge.pop(0)
#             #
#             # elif len(on_bridge) == bridge_length:
#             #     print(on_bridge[0], 'pop from on bridge')
#             #     print()
#             #     on_bridge.pop(0)
#             #     on_bridge_second.pop(0)
#             #     on_bridge_weight = on_bridge[0]
#
#             if truck_weights and on_bridge_weight+truck_weights[0] <= weight:
#                 on_bridge_weight += truck_weights[0]
#                 truck = truck_weights.pop(0)
#                 on_bridge.append(truck)
#                 if idx == 0:
#                     new_second = second + bridge_length + idx
#                     second = new_second
#                 else:
#                     new_second += 1
#                 on_bridge_second.append(new_second)
#
#             else:
#                 if on_bridge and on_bridge_second[0] == second:
#                     print(on_bridge[0], 'pop from on bridge')
#                     print()
#                     on_bridge.pop(0)
#                     answer = on_bridge_second[-1]
#                     on_bridge_second.pop(0)
#
#                     on_bridge_weight = sum(on_bridge)
#                     if on_bridge:
#                         second += 1
#                 break
#
#             # second = second + bridge_length + idx + 1
#             idx += 1
#             print('-'*20)
#             print('on bridge', on_bridge)
#             print('truck weights:', truck_weights)
#             print('second: ', second)
#             print('new second: ', new_second)
#             print('on bridge second: ', on_bridge_second)
#
#             print('-' * 20)
#             print()
#     return answer

# version 3
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     second = 1
#     queue = deque(truck_weights)
#     on_bridge = []
#     weight_sum = 0
#
#     while queue:
#
#         if on_bridge:
#             on_bridge.pop(0)
#             weight_sum = sum([i[0] for i in on_bridge])
#             if on_bridge:
#                 second = on_bridge[-1][1]
#         print('after pop on bridge', on_bridge)
#
#         # if len(on_bridge) < bridge_length:
#         #     second = on_bridge[-1][2]
#         #     print('after iter not equal', second)
#         # elif len(on_bridge) == bridge_length:
#         #     second = on_bridge[-1][1]
#         #     print('after iter equal', second)
#
#         for i in range(bridge_length):
#             if queue:
#                 truck = queue.popleft()
#                 if weight_sum + truck <= weight:
#                     weight_sum += truck
#                     if on_bridge:
#                         second += 1
#                         new_second = second
#                         on_bridge.append([truck, new_second, new_second+bridge_length])
#                         # second = new_second
#                         print('second not empty on bridge', new_second)
#                         print()
#                     else:
#                         on_bridge.append([truck, second, second+bridge_length])
#                         print('second empty on bridge', second)
#                         print()
#                 else:
#                     queue.appendleft(truck)
#
#                     second = on_bridge[-1][1]
#                     print('second over weight', second)
#                     print()
#                     break
#                 print(on_bridge)
#         second = on_bridge[-1][2]
#         print(on_bridge)
#
#     print('end process', on_bridge)
#     answer = on_bridge[-1][2]
#     return answer

# version 4
# def solution(bridge_length, weight, truck_weights):
#     answer = 1
#
#     queue = deque(truck_weights)
#     on_bridge = deque([], maxlen=bridge_length)
#     end_time = deque([], maxlen=bridge_length)
#     cross_bridge = []
#     iters = 0
#     while queue:
#
#         for i in range(bridge_length):
#             if end_time and end_time[0][1] == answer:
#                 on_bridge.popleft()
#                 end_time.popleft()
#                 if end_time and iters > 0:
#                     answer = end_time[-1][0]
#             truck = queue.popleft()
#
#             if sum(on_bridge) + truck <= weight:
#                 on_bridge.append(truck)
#                 if end_time:
#                     print('in for ', answer)
#                     new_answer = answer + i
#                     end_time.append([new_answer, new_answer + bridge_length])
#                 else:
#                     end_time.append([answer, answer + bridge_length])
#
#             else:
#                 queue.appendleft(truck)
#                 answer = end_time[0][1]
#
#             if not queue or sum(on_bridge) == weight:
#                 print('break')
#                 break
#             print('answer', answer)
#             print(on_bridge)
#             print(end_time)
#         iters += 1
#
#         print('after while answer', answer)
#         print(on_bridge)
#         print(end_time)
#         # answer = end_time[-1][0]
#     answer = end_time[-1][1]
#     return answer

# version 5


def solution(bridge_length, weight, truck_weights):
    elapsed_time = 0

    on_bridge = deque()
    truck_queue = deque(truck_weights)
    end_time = deque()

    while True:
        elapsed_time += 1

        if end_time:
            first_elements_end_time = end_time[0][1]
            if first_elements_end_time == elapsed_time:
                on_bridge.popleft()
                end_time.popleft()

        if truck_queue and sum(on_bridge) + truck_queue[0] <= weight:
            on_bridge.append(truck_queue.popleft())

            end_time.append([elapsed_time, elapsed_time+bridge_length])

        if not on_bridge:
            break

    return elapsed_time

bridge_lengths = [2,100, 100, 3]
weights = [10, 100, 100, 10]
truck_weight=[[7,4,5,6], [10],[10,10,10,10,10,10,10,10,10,10], [3,4,5,3]]

for b, w, t in zip(bridge_lengths, weights, truck_weight):
    print(t)
    ans = solution(b,w,t)
    print('answer', ans)