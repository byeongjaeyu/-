m = int(input())
mod_num = 1000000007
ans = 0

def solution(sqr):
    if sqr == 0 or sqr == 1:
        return n%mod_num
    else:
        if sqr%2==0:
            return (solution(sqr//2)**2)%mod_num
        else:
            return (n*(solution(sqr-1)))%mod_num


for test in range(m):
    n,s = map(int, input().split())
    val = solution(mod_num - 2)
    ans += (s*val)%mod_num
    ans %= mod_num
print(ans)