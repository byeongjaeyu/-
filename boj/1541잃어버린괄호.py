from numpy import Inf


def plus(x,y):
    return x+y
def minus(x,y):
    return x-y

def calculate(sts):
    s = sts.split('+')
    sts_sum = 0
    for num in s:
        sts_sum += int(num)
    return sts_sum

s = input()
minus_split = s.split('-')
plus_max = [0,0]
for i in range(1,len(minus_split)):
    val = calculate(minus_split[i])
    if plus_max[0] < val:
        plus_max = [val,i]

ans=  calculate(minus_split[0])

for i in range(1,len(minus_split)):
    if i != plus_max[1]:
        ans -= calculate(minus_split[i])
    else:
        ans -= plus_max[0]

print(ans)