n = int(input())
num_lst = [int(input()) for _ in range(n)]
num_lst.sort()
for i in range(len(num_lst)):
    print(num_lst[i])