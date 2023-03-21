def recursion(s, l, r):
    if l >= r: return l+1, 1
    elif s[l] != s[r]: return l+1, 0
    else: return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


n = int(input())
query = [input() for _ in range(n)]

for q in query:
    trial, is_answer = isPalindrome(q)
    print('{} {}'.format(is_answer, trial))