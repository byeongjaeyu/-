a,b,v = map(int, input().split())
day_h = a-b
print(((v-b)/(a-b))+1) if v-b%a-b == 0 else print(((v-b)/(a-b)))
