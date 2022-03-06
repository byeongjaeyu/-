n = int(input())
ppls = [list(map(str,input().split())) for _ in range(n)]
ppls.sort(key=lambda x:int(x[0]))
for i in range(n):
    print(ppls[i][0],ppls[i][1])