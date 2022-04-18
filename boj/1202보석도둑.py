from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

n,k = map(int, input().split())
q = []
for i in range(n):
    w,v = map(int, input().split())
    heappush(q,[w,v])

bags = [int(input()) for _ in range(k)]
bags.sort()

ans = 0
temp = []

for bag in bags:
    while q and bag>=q[0][0]:
        heappush(temp,-1*heappop(q)[1])
    if temp:
        ans -= heappop(temp)

print(ans)

