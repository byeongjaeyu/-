from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

for test in range(int(input())):
    n = int(input())
    heap = []
    max_heap = []
    visited = [False] * 1000001
    for i in range(n):
        op, n = map(str,input().split())
        n = int(n)
        if op=="I":
            heappush(heap,(n,i))
            heappush(max_heap,(n*-1,i))
            visited[i] = True
        else:
            if n == -1:
                while heap and not visited[heap[0][1]]:
                    heappop(heap)
                if heap:
                    visited[heap[0][1]] = False
                    heappop(heap)
            elif n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)

    while heap and not visited[heap[0][1]]:
        heappop(heap)
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)

    print(-1*max_heap[0][0], heap[0][0]) if heap and max_heap else print('EMPTY')


