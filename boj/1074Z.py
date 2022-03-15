def solution(s:list,e:list,cnt:int):
    d = int(((e[0] - s[0] + 1)**2)/4)
    
    if s[0] == e[0] or s[1] == e[1]:
        return cnt

    if s[0]<=r<=((s[0]+e[0])//2) and s[1]<=c<=((s[1]+e[1])//2):
        val = solution([s[0],s[1]],[((s[0]+e[0])//2),((s[1]+e[1])//2)],cnt)
        return val

    elif s[0]<=r<=((s[0]+e[0])//2) and (((s[1]+e[1])//2)+1) <= c <= e[1]:
        val = solution([s[0],(((s[1]+e[1])//2)+1)],[((s[0]+e[0])//2),e[1]],cnt + d)
        return val

    elif (((s[0]+e[0])//2)+1) <= r <= e[0] and s[1]<=c<=((s[1]+e[1])//2):
        val = solution([(((s[0]+e[0])//2)+1),s[1]],[e[0],((s[1]+e[1])//2)],cnt + (2*d))
        return val

    else:
        val = solution([(((s[0]+e[0])//2)+1),(((s[1]+e[1])//2)+1)],[e[0],e[1]],cnt+(3*d))
        return val


n,r,c = map(int, input().split())
s = [0,0]
e = [(2**n)-1,(2**n)-1]
print(solution(s,e,0))