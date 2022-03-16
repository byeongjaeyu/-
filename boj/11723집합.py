from sys import stdin
input = stdin.readline
n = int(input())
s = set()
for i in range(n):
    op_n = input().split()
    op = op_n[0]
    if len(op_n)>1:
        n = int(op_n[1])
    if op=="add":
        s.add(n)
    elif op=="check":
        if n in s:
            print(1)
        else:
            print(0)
    elif op=="remove":
        if n in s:
            s.remove(n)
    elif op=="toggle":
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif op=="all":
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif op=="empty":
        s = set()
