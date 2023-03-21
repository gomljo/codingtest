import sys


def bisect(arr, target):

    left = 0
    right = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return '1'
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return '0'


num_of_card = int(input())
cards = list(map(int, sys.stdin.readline().split(' ')))

num_of_query_card = int(input())
query_cards = list(map(int, sys.stdin.readline().split(' ')))

cards.sort()

for query_card in query_cards:
    print(bisect(cards, query_card), end='')
