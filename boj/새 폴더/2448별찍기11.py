def solution(n:int):
    

import math
n = int(input())
k = int(math.log2(n/3))
default_height = 3
default_width = 5
cnt = 0
height = default_height;width = default_width
while cnt < k:
    height *= 2
    width = width*2 + 1
    cnt += 1

default_tri = [[" "," ","*"," "," ",],[" ","*"," ","*"," ",],["*","*","*","*","*",]]

map = [[""]*width for _ in range(height)]

solution(0)