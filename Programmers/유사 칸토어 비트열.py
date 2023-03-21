import heapq
from collections import Counter
from collections import deque


def calc_idx(pos, prev_idx, n):
    length = len(prev_idx)
    new_zero_idx=[]
    if pos==2:
        new_zero_idx = list(range(pos*5**(n-1)+1, (pos+1)*5**(n-1)+1))
    else:
        for i in range(length):
            new_zero_idx.append(pos * 5 ** (n - 1) + prev_idx[i])
    return new_zero_idx


def find_zero_idx(prev_zero_idx, n):

    zero_idx = []
    for i in range(5):
        new_zero_idx = calc_idx(i, prev_zero_idx, n)
        zero_idx.extend(new_zero_idx)
    return zero_idx


def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result


def calc_zero_cnt(zero_idx, l, r):
    l_p=0
    r_p=0
    for idx, value in enumerate(zero_idx):
        if value >= l:
            l_p = idx
            break
    for i in range(len(zero_idx)-1, 0, -1):
        if zero_idx[i] <= r:
            r_p = i
            break

    return len(zero_idx[l_p:r_p])

def solution(n, l, r):

    zero_idx = [3, 8, 11, 12, 13, 14, 15, 18, 23]
    if n == 1:
        zero_idx = [3]
    else:
        for i in range(3, n+1):
            zero_idx = find_zero_idx(zero_idx, i)
    zero_cnt=calc_zero_cnt(zero_idx, l, r)

    return r-l-zero_cnt


def fractal(bit_seq):

    new_bit_seq = []
    for bit in bit_seq:

        if bit==1:
            new_bit_seq.extend([1,1,0,1,1])
        else:
            new_bit_seq.extend([0,0,0,0,0])
    return new_bit_seq

def validate(n, l, r):
    bit_seq = [1]
    for i in range(n):
        bit_seq=fractal(bit_seq)

    valid_zero_idx = []
    for i in range(len(bit_seq)):
        if bit_seq[i]==0:
            valid_zero_idx.append(i+1)
    # print('expe',valid_zero_idx)
    # print(Counter(bit_seq[l-1:r+1]))
    return Counter(bit_seq[l-1:r])[1], valid_zero_idx

n = 4
l = 17
r = 123

answer = solution(n, l, r)
expected_answer, valid_bit = validate(n, l, r)
print(answer)
print(expected_answer)
