N = int(input())
li1 = list(map(int, input().split()))
M = int(input())
li2 = list(map(int, input().split()))
d = {}

for n in li1:
    d[n] = d.get(n, 0) + 1
print(' '.join(str(d[m]) if m in d else '0' for m in li2))