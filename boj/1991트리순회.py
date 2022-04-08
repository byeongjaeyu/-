n = int(input())
tree = dict()
for i in range(n):
    p,l,r = map(str,input().split())
    if l=='.' and r!='.':
        tree[p] = [None,r]
    elif r=='.' and l!='.':
        tree[p] = [l,None]
    elif r=='.' and l=='.':
        tree[p] = [None,None]
    else:
        tree[p] = [l,r]

def read1(node:str):
    global ans
    if node == None:
        return
    left = tree[node][0]
    right = tree[node][1]
    ans.append(node)
    read1(left)
    read1(right)

def read2(node:str):
    global ans
    if node == None:
        return
    left = tree[node][0]
    right = tree[node][1]
    read2(left)
    ans.append(node)
    read2(right)

def read3(node:str):
    global ans
    if node == None:
        return
    left = tree[node][0]
    right = tree[node][1]
    read3(left)
    read3(right)
    ans.append(node)



ans = []
read1('A')
print(''.join(map(str,ans)))
ans.clear()

read2('A')
print(''.join(map(str,ans)))
ans.clear()

read3('A')
print(''.join(map(str,ans)))