n,m = map(str,input().split())
a = int(n[::-1])
b = int(m[::-1])
print(a) if a>b else print(b)