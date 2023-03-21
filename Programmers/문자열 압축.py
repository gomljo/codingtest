from collections import deque


def get_element(queue, window_size):
    return queue[:window_size]


def remove_element(queue, window_size):
    new_queue = queue[window_size:]
    return new_queue


def add_element(stack, element):
    stack.append(element)
    return stack


def compress(window_size, text):
    queue = text
    stack = []
    cnt = 0
    text_length = len(text)
    compress_string = ""
    # print(get_element(queue, window_size))
    new_element = get_element(queue, window_size)
    while cnt < 2:
        if stack[-1] == new_element:
            print(stack[-1])
            print(queue[:window_size])
            print('same')
            stack = add_element(stack, new_element)
            queue = remove_element(queue, window_size)
        elif stack == []:
            stack = add_element(stack, new_element)
            queue = remove_element(queue, window_size)
        # while queue:

        # if stack[-1] == queue[:window_size]:
        #     same_element = queue[:window_size]
        #     stack.append(same_element)
        #     queue = queue[window_size]
        # elif stack==[]:
        #     stack.append(queue[:window_size])
        #     queue=queue[window_size:]
        # else:
        #     letter = stack[-1]
        #     length = len(stack)
        #     new_element = queue[:window_size]
        #     stack = [new_element]
        #     queue = queue[window_size:]
        cnt += 1
    print(stack)
    return compress_string


def solution(s):
    answer = 0

    for window_size in range(1, len(s) // 2 + 1):
        compress(window_size, s)

    return answer


s = "aabbaccc"
solution(s)