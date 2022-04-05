from sys import setrecursionlimit
setrecursionlimit(2501)
message = list(input())
length = len(message)
dp = [[0]*length for _ in range(length)]
for i in range(length):
    dp[i][i] = 1

for i in range(length):
    for j in range(length):
        if i<length and j<length and i>j:
            if i == j+1:
                if(message[i]==message[j]):
                    dp[j][i] = 1
            else:
                if(dp[j+1][i-1]==1 and message[i]==message[j]):
                    dp[j][i] = 1

ans_dp = [0xffffffff]*(length+1)

ans_dp[0] = 0

for i in range(1,length+1):

    for j in range(i+1,length+1):
        if dp[i-1][j-1] == 1:
            ans_dp[j] = min(ans_dp[j],ans_dp[i-1]+1)

    ans_dp[i] = min(ans_dp[i-1]+1,ans_dp[i])

print(ans_dp[-1])

# # from heapq import heappop,heappush
# for i in range(length):
#     print(dp[i])
# ans = 0xffffffff

# # def bfs():
# #     global ans
# #     while q:
# #         minus_idx,cnt = heappop(q)
# #         if cnt > ans:
# #             continue
# #         for idx2 in range(-1*minus_idx,length):
# #             if dp[-1*minus_idx][idx2] == 1:
# #                 if idx2 == length-1:
# #                     ans = min(ans,cnt+1)
# #                 else:
# #                     heappush(q,[-1*(idx2+1),cnt+1])


# # q = []
# # for i in range(length):
# #     if i>ans:
# #         continue
# #     heappush(q,[-1*i,i])
# #     bfs()
# #     q.clear()
# # print(ans)



# def dfs(idx:int):
#     global cnt, ans
#     if idx == length:
#         ans = min(ans,cnt)
#         return
#     if cnt >= ans:
#         return
#     for idx2 in range(length-1,idx-1,-1):
#         if dp[idx][idx2] == 1:
#             cnt += 1
#             dfs(idx2+1)
#             cnt -= 1


# for i in range(length):
#     cnt = i
#     if i<length-1 and cnt+1 >= ans: continue
#     if cnt>=ans:
#         continue
#     dfs(i)

# print(ans)
