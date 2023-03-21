
n = int(input())

bucket_5 = 5
bucket_3 = 3

max_5 = 1001
max_3 = 5000//3+1
answer= []
for i in range(max_5):
    for j in range(max_3):
        if n - (bucket_3 * j + bucket_5 * i)==0:
            answer.append(i+j)

if not answer:
    print(-1)
else:
    print(min(answer))