n = int(input())
lev = 0
s = 1
while True:
    if n <= s:
        break
    lev += 1
    s += 6*(lev-1)
print(int(lev)) if n != 1 else print(1)