n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
lines = []

def distance(x:list,y:list):
    return (abs( ((x[0]-y[0])**2 + (x[1]-y[1])**2))**0.5 )

for i in range(len(stars)):
    for j in range(i+1,len(stars)):
        lines.append([i,j,distance(stars[i],stars[j])])
        lines.append([j,i,distance(stars[i],stars[j])])

parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a,b):
    roota = find(a)
    rootb = find(b)
    if roota<rootb:
        parent[rootb] = roota
    else:
        parent[roota] = rootb

lines.sort(key=lambda x:x[2])
# print(lines)

ans = 0
for line in lines:
    a,b,cost = line
    if find(a) != find(b):
        union(a,b)
        ans += cost

print(round(ans,2))