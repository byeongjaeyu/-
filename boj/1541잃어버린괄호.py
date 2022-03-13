def plus(x,y):
    return x+y
def minus(x,y):
    return x-y

s = input()
plus_split = s.split('+')
minus_split = []
for plus in plus_split:
    minus_split.append(plus.split('-'))

print(minus_split)