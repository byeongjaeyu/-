s = input()
operator = {'+':0,'-':0,'*':1,'/':1}
stack = []
ans = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        while stack:
            p = stack.pop(-1)
            if p == '(':
                break
            else:
                ans.append(p)
    elif s[i] == '+' or s[i] == '-':
        while stack:
            p = stack.pop(-1)
            if p!='(' and operator[p] >= operator[s[i]]:
                ans.append(p)
            else:
                stack.append(p)
                break
        stack.append(s[i])
    elif s[i] == '*' or s[i] == '/':
        while stack:
            p = stack.pop(-1)
            if p!='(' and operator[p] >= operator[s[i]]:
                ans.append(p)
            else:
                stack.append(p)
                break
        stack.append(s[i])
    else:
        ans.append(s[i])
while stack:
    ans.append(stack.pop(-1))
print(ans)