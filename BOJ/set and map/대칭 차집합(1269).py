N, M = map(int, input().split(' '))

A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

intersection = A.intersection(B)

print(len(A) + len(B) - 2*len(intersection))
