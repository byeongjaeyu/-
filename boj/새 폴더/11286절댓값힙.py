from heapq import heappush, heappop
from sys import stdin

input = stdin.readline

heap = []

n = int(input())

for i in range(n):
    num = int(input())
    if num:
        if num > 0:
            heappush(heap,[abs(num),1])
        else:
            heappush(heap,[abs(num),-1])
    else:
        if not len(heap):
            print(0)
        else:
            val = heappop(heap)
            if val[1] > 0:
                print(val[0])
            else:
                print(-1*val[0])