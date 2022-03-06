from collections import deque
n = int(input())
q = deque()
for num in range(1,n+1):
    q.append(num)
while len(q)!=1:
    p = q.popleft()
    if(len(q)==1):
        break
    p2 = q.popleft()
    q.append(p2)

print(q[0])