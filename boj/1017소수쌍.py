n = int(input())
primes = list(map(int, input().split()))
max_num = 2000
is_prime = [True]*(max_num+1)
for i in range(2,max_num+1):
    if is_prime[i]:
        j = 2
        while i*j <= max_num:
            is_prime[i*j] = False
            j += 1
is_matched = [False]*(n)


