message = input()
bomb = input()
stack = []
ml = len(message)
bl = len(bomb)

for char in message:
    stack.append(char)
    if char == bomb[-1] and "".join(stack[-1*bl:]) == bomb:
        del stack[-1*bl:]

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))