n = int(input())
heap = []
for i in range(n):
    n = int(input())
    if n:
        heap.append(n)
    else:
        if heap:
            heap.sort()
            print(heap.pop(0))
        else:
            print(0)