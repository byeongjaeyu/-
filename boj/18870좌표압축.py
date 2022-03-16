n = int(input())
x_lst = list(map(int, input().split()))
x_lst_sort = sorted(x_lst)
ans_dict = dict()
cnt = 0
for x in x_lst_sort:
    if ans_dict.get(x) == None:
        ans_dict[x] = cnt
        cnt += 1
ans_lst = [0] * n
for i in range(n):
    ans_lst[i] = ans_dict[x_lst[i]]
print(*ans_lst)
