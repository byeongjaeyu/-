n = int(input())
stack = []
ans = []
now_num = 1
flag = True
for i in range(n):
    num = int(input())
    while now_num <= num:
        stack.append(now_num)
        ans.append("+")
        now_num += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        flag = False
        break

if flag == True:
    for i in ans:
        print(i)
