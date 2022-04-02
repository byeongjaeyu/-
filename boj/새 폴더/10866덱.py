from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    inp = list(map(str,sys.stdin.readline().split()))
    if len(inp) == 2:
        method, num = inp
        num = int(num)
        if method == "push_front":
            q.appendleft(num)
        else:
            q.append(num)
    else:
        method = inp[0]
        if method == "front":
            if len(q) > 0:
                print(q[0])
            else:
                print(-1)
        elif method == "back":
            if len(q) > 0:
                print(q[-1])
            else:
                print(-1)
        elif method == "size":
            print(len(q))
        elif method == "empty":
            print(1) if len(q) == 0 else print(0)
        elif method == "pop_front":
            if len(q) > 0:
                print(q.popleft())
            else:
                print(-1)
        else:
            if len(q) > 0:
                print(q.pop())
            else:
                print(-1)