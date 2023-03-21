n = int(input())
words = [input() for _ in range(n)]

words_sorted = sorted(set(words), key=lambda x: (len(x), x))
for word in words_sorted:
    print(word)