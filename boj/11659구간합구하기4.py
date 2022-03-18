from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
num_lst = list(map(int, input().split()))
sum_lst = [0]*n
sum_lst[0] = num_lst[0]
for i in range(1,n):
    sum_lst[i] = sum_lst[i-1] + num_lst[i]
for i in range(m):
    a,b = map(int, input().split())
    a -= 1; b -= 1
    if a == 0:
        print(sum_lst[b])
    else:
        print(sum_lst[b]-sum_lst[a-1])
