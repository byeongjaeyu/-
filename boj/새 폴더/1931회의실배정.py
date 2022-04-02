n = int(input())


dis_lst = [list(map(int ,input().split())) for _ in range(n)]

dis_lst.sort(key=lambda x:(x[1],x[0]))

end_point = dis_lst[0][1]

ans = 1

for i in range(1,n):
    if dis_lst[i][0] >= end_point:
        ans += 1
        end_point = dis_lst[i][1]
        
print(ans)
