n = int(input())
arr = [0]*5
for i in range(n):
    x,y = map(int, input().split())
    arr[i] = [x,y]

arr.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(*arr[i])
