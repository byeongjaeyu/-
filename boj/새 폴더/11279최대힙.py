from heapq import heappush, heappop
from sys import stdin

n = int(stdin.readline())
heap = []
for i in range(n):
    op = int(stdin.readline())
    if not op:
        if not heap:
            print(0)
        else:
            print(-1*heappop(heap))
    else:
        heappush(heap,-1*op)