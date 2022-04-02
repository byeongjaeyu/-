from math import gcd
from sys import stdin
input = stdin.readline
def lcm(x,y):
    return (x*y) // gcd(x,y)
for test in range(int(input())):
    m,n,x,y = map(int, input().split())
    lc = lcm(m,n)
    i = x
    while True:
        if i > lc:
            print(-1)
            break
        else:
            if i%n == y%n:
                print(i)
                break
            i += m

