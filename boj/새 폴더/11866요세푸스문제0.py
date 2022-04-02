n,k = map(int, input().split())
ppls = [i for i in range(1,n+1)]
idx = k-1
print("<",end="")
while ppls:
    print(ppls.pop(idx),end="")
    if len(ppls) == 0:
        break
    print(", ",end="")
    idx += k-1
    if idx > len(ppls)-1:
       idx = idx % len(ppls)
print(">")
