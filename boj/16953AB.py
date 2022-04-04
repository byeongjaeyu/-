a,b = map(int, input().split())
from heapq import heappop, heappush
q = []
heappush(q,[1,a])
visited = set()
visited.add(a)
flag = True
while q:
    cnt,num = heappop(q)
    if num == b:
        flag = False
        print(cnt)
        break
    num1 = num*2
    if num1 not in visited and num1 <= 10**9:
        visited.add(num1)
        heappush(q,[cnt+1,num1])
    num2 = (num*10)+1
    if num2 not in visited and num2 <= 10**9:
        visited.add(num2)
        heappush(q,[cnt+1,num2])

if flag:
    print(-1)


