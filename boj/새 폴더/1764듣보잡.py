n,m = map(int, input().split())
듣 = set()
보 = set()
for i in range(n):
    듣.add(input())
for i in range(m):
    보.add(input())

듣보잡 = list(듣 & 보)
듣보잡.sort()
print(len(듣보잡))
for 듣보 in 듣보잡:
    print(듣보)

