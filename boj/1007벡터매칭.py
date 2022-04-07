from math import sqrt
from sys import stdin
input = stdin.readline
def getlength(v):
    return (sqrt( (abs(v[0])**2) + (abs(v[1])**2) ))

def getvector(v1:list,v2:list):
    return ([v2[0]-v1[0],v2[1]-v1[1]])

def solution(cnt:int,idx:int):
    global ans
    if cnt == (n//2)+1:
        sel = [0,0]
        notsel = [0,0]
        for i in range(n):
            if visited[i]:
                sel[0] += dots[i][0]
                sel[1] += dots[i][1]
            else:
                notsel[0] += dots[i][0]
                notsel[1] += dots[i][1]
        ans = min(ans,getlength(getvector(sel,notsel)),getlength(getvector(notsel,sel)))

        return
    for i in range(idx,n):
        if visited[i]:
            continue
        visited[i] = 1
        solution(cnt+1,i+1)
        visited[i] = 0

for test in range(int(input())):
    n = int(input())
    dots = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    ans = 0xffffffff
    solution(1,0)
    print(round(ans,7))