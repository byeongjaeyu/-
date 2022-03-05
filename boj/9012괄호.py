for test in range(int(input())):
    s = input()
    left = 0
    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        else:
            if not left:
                print('NO')
                break
            else:
                left -= 1
    else:
        if left:
            print('NO')
        else:
            print('YES')