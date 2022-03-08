n = int(input())

cnt1=0;cnt2=0;cnt3=0

while True:
    if n == 0:
        break
    if n<0:
        cnt3 = -1
    if (n%5)%3 == 0:
        cnt1 += n//5
        cnt2 += (n%5)//3
        break
    else:
        n -= 3
        cnt2 += 1

print(cnt3) if cnt3<0 else print(cnt1+cnt2)