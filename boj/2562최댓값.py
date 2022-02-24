ans = 0
ans_idx = 0
for i in range(9): 
    n = int(input())
    print(n,i)
    if ans < n:
        ans = n
        ans_idx = i

print(ans)
print(i)

