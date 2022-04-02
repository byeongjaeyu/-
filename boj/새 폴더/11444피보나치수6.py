fibos = {0:0,1:1,2:1,3:2,4:3}

def fibo(n):
    if fibos.get(n):
        return fibos[n]
    else:
        k = (n+1)//2
        fibos[n] = (fibo(k) * fibo(n+1-k) + fibo(k-1) * fibo(n-k)) % 1000000007
        return fibos[n]

n = int(input())
print(fibo(n))