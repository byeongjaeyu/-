n = int(input())
heap = list(map(int, input().split()))
heap.sort()
ans = 0
add = 0
for time in heap:
    add += time
    ans += add

print(ans)
