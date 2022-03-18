for test in range(int(input())):
    n = int(input())
    cloths = dict()
    for i in range(n):
        a,b = input().split()
        if cloths.get(b) == None:
            cloths[b] = [a]
        else:
            cloths[b].append(a)
    
    ans = 1
    for key in cloths:
        ans *= (len(cloths[key])+1)
    ans -= 1

    print(ans)