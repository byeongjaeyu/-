from heapq import heappop, heappush

for test in range(int(input())):
    n = int(input())
    heap = []
    max_heap = []
    for i in range(n):
        op, n = map(str,input().split())
        n = int(n)
        if op=="I":
            heappush(heap,n)
            heappush(max_heap,n*-1)
        else:
            if heap:
                if n == -1:
                    min_val = heappop(heap)

                else:
                    max_val = heappop(max_heap)

    print("EMPTY") if not heap else print(heappop(max_heap)*-1, heappop(heap))


