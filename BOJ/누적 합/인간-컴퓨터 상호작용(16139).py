# from copy import deepcopy
# from collections import defaultdict
# sentence = list(input())
#
# num_of_query = int(input())
# queries = []
#
# for i in range(num_of_query):
#     query = input().split(' ')
#     alphabet, s, e = query[0], int(query[1]), int(query[2])
#     queries.append([alphabet, s, e])
# num_of_alphabet = 26
# alpha_dict = defaultdict(int)
#
# prefix_alpha = [deepcopy(alpha_dict)]
# for alphabet in list(sentence):
#     alpha_dict[alphabet] += 1
#     prefix_alpha.append(deepcopy(alpha_dict))
#
#
# for query in queries:
#     alphabet, s, e = query[0], query[1], query[2]
#     e_cnt, s_cnt = 0, 0
#     if alphabet in prefix_alpha[e+1].keys():
#
#         e_cnt = prefix_alpha[e+1][alphabet]
#     if alphabet in prefix_alpha[s].keys():
#
#         s_cnt = prefix_alpha[s][alphabet]
#     print(e_cnt-s_cnt)
import sys
input = sys.stdin.readline

sentence = input().rstrip()

num_of_query = int(input())

queries = []
prefix_list = [[0] * 26]

for idx, s in enumerate(sentence):
    new_list = prefix_list[-1][:]
    new_list[ord(s) - 97] += 1
    prefix_list.append(new_list)

for i in range(num_of_query):
    query = input().split(' ')
    alphabet, s, e = query[0], int(query[1]), int(query[2])
    e_cnt = prefix_list[e+1][ord(alphabet) - 97]
    s_cnt = prefix_list[s][ord(alphabet) - 97]
    print(e_cnt-s_cnt)