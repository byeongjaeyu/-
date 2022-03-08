n,m = map(int, input().split())
tree_lst = list(map(int, input().split()))

s = 0
e = 1000000000
while True:
    if s>e:
        mid = e
        break
    mid = (s+e)//2
    pr = 0
    for tree in tree_lst:
        if tree>mid:
            pr += tree-mid
    
    if pr >= m:
        s = mid + 1

    else:
        e = mid - 1
        
print(mid)
