n = int(input())
num_lst = list(map(int ,input().split()))
m = int(input())
num_lst2 = list(map(int, input().split()))

ans = [0]*m

num_dict = dict()
for idx in range(len(num_lst2)):
    if num_dict.get(num_lst2[idx]) == None:
        num_dict[num_lst2[idx]] = [idx]
    else:
        num_dict[num_lst2[idx]].append(idx)
    

for num in num_lst:
    value = num_dict.get(num)
    if value != None:
        for v in value:
            ans[v] += 1
    

print(*ans)