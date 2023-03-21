import sys
from collections import defaultdict

num_of_card = int(input())
cards = list(map(int, sys.stdin.readline().split(' ')))
card_dict = defaultdict(int)
for card in cards:
    card_dict[card] += 1

num_of_query_card = int(input())
query_cards = list(map(int, sys.stdin.readline().split(' ')))

for query_card in query_cards:
    if query_card in card_dict.keys():
        print(card_dict[query_card], end=' ')
    else:
        print('0', end=' ')