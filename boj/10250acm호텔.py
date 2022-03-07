for test in range(int(input())):
    h,w,n = map(int, input().split())
    f = str(n%h)
    room = (n//h)+1
    ans = f
    if room<10:
        ans += '0{}'.format(str(room))
    else:
        ans += str(room)
    print(ans)
