ans = 0
ans_idx = 0
for i in range(9): 
    n = int(input())
    if ans < n:
        ans = n
        ans_idx = i

print(ans)
print(ans_idx+1)

