n = int(input())
m = int(input())
s = list(input())

i = 0
cnt = 0
flag = False
while True:
    if i >= m-1:
        break
    if not flag and s[i] == 'I':
        oi_cnt = 0
        while True:
            if oi_cnt == n:
                break
            if i+2 <= m-1 and s[i+1] == 'O' and s[i+2] == 'I':
                oi_cnt += 1
                i += 2
            else:
                break
        
        if oi_cnt == n:
            flag = True
            i += 1
            cnt += 1
            continue
        else:
            i += 1
            continue
    
    elif not flag and s[i] == 'O':
        i += 1
        continue
    
    elif flag:
        while True:
            if i+1 <= m-1 and s[i] == 'O' and s[i+1] == 'I':
                cnt += 1
                i += 2
            else:
                flag = False
                break

print(cnt)
