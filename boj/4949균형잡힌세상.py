while True:
    st = input()
    if len(st) == 1:
        break
    stack = []
    for s in st:
        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if len(stack)>0:
                if stack[-1] != '(':
                    print('no')
                    break
                else:
                    stack.pop(-1)
            else:
                print('no')
                break
        elif s == "]":
            if len(stack)>0:
                if stack[-1] != '[':
                    print('no')
                    break
                else:
                    stack.pop(-1)
            else:
                print('no')
                break
    else:
        print('yes')
        