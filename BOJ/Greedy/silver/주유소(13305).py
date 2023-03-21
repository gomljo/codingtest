# first solution(success only first task)
# num_of_city = int(input())
# roads = [int(x) for x in input().split(' ')]
# price_per_station = [int(x) for x in input().split(' ')]
# price_per_station = price_per_station[:-1]
# destination = sum(roads)
#
# prices = []
# on_road = []
# for road, price in zip(roads, price_per_station):
#     if on_road:
#         price_for_end = destination * price + on_road[-1]
#         price_for_next = road * price + on_road[-1]
#     else:
#         price_for_end = destination * price
#         price_for_next = road * price
#
#     prices.append(price_for_end)
#     on_road.append(price_for_next)
#
#     destination -= road
# minimum_price = min(prices)
# print(minimum_price)

# second solution
# use cumulative summation
# idea
# add previous station's oil consumption to next station's oil consumption

# example

# price: 5 - 2 - 4 - 1 -3
# Km: 2 - 3 - 1 - 3

# first station's oil consumption
# [5 X 2, 5X(2+3), 5 X (2+3+1), 5 X (2+3+1+3)] => [0, 10, 15, 25, 45]

# second station's oil consumption
# we use oil for moving first station to second station.
# So, add first station's oil consumption for moving second station to second station's oil consumption
# [10, 10 + 2 X 3, 10 + 2 X 4, 10 + 2 X 7] = [0, 10, 16, 18, 24]

# third station's oil consumption
# we use oil for moving second station to third station.
# So, add second station's oil consumption for moving third station to third station's oil consumption
# [10, 16, 16 + 4 X 1, 16 + 4 X 4] = [0, 10, 16, 20, 32]

# Every stop before the last stop has one price.
# So, we need to examine stops before the last stop.
# every station's length is number of cities.
# target stop's position is station's length - 2. Because array index starts with 0.
# candidates are 25, 18, 20.
# oil consumption for last stop is 1 X 3 => 3
# result that adding oil consumption for last stop to candidates is 28, 21, 23

# The first value 28 is the result of refueling at the first gas station.

# The second value 21 is the result of refueling at the first gas station to second station
# and at the second gas station to fourth station.

# The third value 23 is the result of refueling at the every gas station to next station.

# So, the minimum value 21 is the answer we want

# implementation
# import math
#
# num_of_city = int(input())
# roads = [int(x) for x in input().split(' ')]
# price_per_station = [int(x) for x in input().split(' ')]
# prefix_road = []
# road_sum = 0
#
# if sum(price_per_station) == len(price_per_station):
#     print(sum(roads))
# else:
#     for road in roads:
#         road_sum += road
#         prefix_road.append(road_sum)
#
#     price_matrix = [0]
#     price_matrix.extend([math.inf]*(num_of_city-1))
#     station_matrix = []
#
#     for idx, price in enumerate(price_per_station):
#         road_sum = 0
#         prev_cost = price_matrix[idx]
#         for road_pos in range(idx, len(roads)):
#             road_sum += roads[road_pos]
#             current_cost = price * road_sum + prev_cost
#             if price_matrix[road_pos+1] > current_cost:
#                 price_matrix[road_pos+1] = current_cost
#     print(price_matrix[-1])

# third solution
import math

num_of_city = int(input())
roads = [int(x) for x in input().split(' ')]
price_per_station = [int(x) for x in input().split(' ')]

cur_price = math.inf
cur_pos = []
for idx, price in enumerate(price_per_station[:-1]):
    if cur_price > price:
        cur_price = price
        cur_pos.append(idx)
answer = 0

cur_pos.append(len(price_per_station))
for i in range(len(cur_pos)-1):
    answer += price_per_station[cur_pos[i]] * sum(roads[cur_pos[i]:cur_pos[i+1]])

print(answer)

