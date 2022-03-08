k = int(input())
stack = []
ans = 0
for i in range(k):
    num = int(input())
    if num != 0:
        stack.append(num)
        ans += num
    else:
        ans -= stack.pop(-1)

print(ans)
