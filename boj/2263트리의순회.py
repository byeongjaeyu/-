from sys import setrecursionlimit
setrecursionlimit(10**6)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
idx_save = [0]*(n+1)
for i in range(n):
    idx_save[inorder[i]] = i

ans = []

def solution(in_start,in_end,p_start,p_end):
    if (in_start>in_end) or (p_start>p_end):
        return
    
    parent = postorder[p_end]
    ans.append(parent)
    left = idx_save[parent] - in_start
    right = in_end - idx_save[parent]

    solution(in_start,in_start+left-1,p_start,p_start+left-1)
    solution(in_end-right+1,in_end,p_end-right,p_end-1)
solution(0,n-1,0,n-1)

print(' '.join(map(str,ans)))