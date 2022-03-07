n,k = map(int, input().split())
ppls = [i for i in range(1,n+1)]
idx = 2
print("<",end="")
while ppls:
    print(ppls.pop(idx),end="")
    if len(ppls) == 0:
        break
    print(", ",end="")
    idx += 2
    if idx > len(ppls)-1:
       idx = idx % len(ppls)
print(">")
