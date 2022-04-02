chess1 = [
    ["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"]
]

chess2 = [
    ["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"]
]


def solution(i1:int,i2:int):
    global ans
    cnt1 = 0;cnt2 = 0
    for idx1 in range(8):
        for idx2 in range(8):
            if input_lst[i1+idx1][i2+idx2] != chess1[idx1][idx2]:
                cnt1 += 1
            if input_lst[i1+idx1][i2+idx2] != chess2[idx1][idx2]:
                cnt2 += 1
    ans = min(cnt1,cnt2,ans)
    

n,m = map(int, input().split())
input_lst = [list(input()) for _ in range(n)]

ans = 2500
for i1 in range(n-8+1):
    for i2 in range(m-8+1):
        solution(i1,i2)

print(ans)