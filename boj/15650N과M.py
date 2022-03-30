n,m = map(int, input().split())
def solution(i:int,j:int,lst:list):
    if j == m:
        print(*lst)
    else:
        for k in range(i+1,n+1):
            solution(k,j+1,lst+[k])
for i in range(1,n+1):
    solution(i,1,[i])