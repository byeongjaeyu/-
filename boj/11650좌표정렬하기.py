n = int(input())
input_lst = [list(map(int, input().split())) for _ in range(n)]
input_lst.sort(key = lambda x:(x[0],x[1]))
for i in range(n):
    print(*input_lst[i])