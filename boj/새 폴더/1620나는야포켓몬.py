n,m = map(int, input().split())
pocketmon_lst = dict()
for _ in range(n):
    pocketmon_lst[input()] = _+1

keys = list(pocketmon_lst.keys())

for i in range(m):
    a = input()
    try:
        a = int(a)
        print(keys[a-1])
    except:
        print(pocketmon_lst[a])

