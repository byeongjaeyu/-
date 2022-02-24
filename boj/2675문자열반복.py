tc = int(input())
for t in range(tc):
    n,s = map(str,input().split())
    n = int(n)
    ans = ''
    for i in range(len(s)):
        ans += n*s[i]
    print(ans)