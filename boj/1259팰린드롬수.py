flag = True
while flag:
    n = input()
    if n == "0":
        flag = False
        continue
    rn = n[::-1]
    if n == rn:
        print('yes')
    else:
        print('no')