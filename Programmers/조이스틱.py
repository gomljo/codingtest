def solution(name):
    answer = 0
    cnt = 0
    name = list(name)
    total_length = len(name)
    while name:
        a = name.pop(0)
        print(cnt)
        if a == 'A' and (cnt+1 + len(name)) <= (cnt+2+len(name)):
            answer+=cnt+1
            cnt=0
            while name[0] == 'A':
                name.pop(0)
                print(name)
            name = [a for a in reversed(name)]
            print(name)
        else:
            print('move', min(abs(ord('A') - ord(a)), abs(ord('Z') - ord(a))+1))
            answer += min(abs(ord('A') - ord(a)), abs(ord('Z') - ord(a))+1)
            print(answer)
            if len(name) > 0:
                cnt+=1
    answer+=cnt
    print(answer)
    return answer


n = 'JEROEN'

ans = solution(n)
print(ans)