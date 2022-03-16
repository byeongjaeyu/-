import heapq
import sys
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(heap,n)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)