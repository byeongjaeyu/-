n,x = map(int, input().split())
lst = list(map(int, input().split()))
for num in lst:
    if num < x:
        print(num,end="")