from collections import deque

def D(s:int):
    double = s*2
    if(double)>9999:
        return (double%10000)
    return (double)

def S(s:int):
    minus1 = s-1
    if(minus1==-1):
        return (9999)
    return (minus1)

def L(s:int):
    p = s%1000
    p2 = s//1000
    return (p*10+p2)

def R(s:int):
    p = s%10
    p2 = s//10
    return (p*1000+p2)



def BFS():
    while q:
        p1,p2 = q.popleft()
        if p1 == b:
            print(p2)
            return
        
        for i in range(4):
            if i==0:
                save = D(p1)
                if visited[save] == 0:
                    q.append([save,p2+"D"])
                    visited[save] = 1
            elif i==1:
                save = S(p1)
                if visited[save] == 0:
                    q.append([save,p2+"S"])
                    visited[save] = 1
            elif i==2:
                save = L(p1)
                if visited[save] == 0:
                    q.append([save,p2+"L"])
                    visited[save] = 1
            else:
                save = R(p1)
                if visited[save] == 0:
                    q.append([save,p2+"R"])
                    visited[save] = 1



for test in range(int(input())):

    a,b = map(int,input().split())
    ans = []
    visited = [0]*10000
    
    q = deque()
    q.append([a,""])
    visited[a] = 1

    BFS()
