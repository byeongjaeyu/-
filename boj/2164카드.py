n = int(input())
num_lst = [num for num in range(1,n+1)]
num_lst.sort()
while True:
    p = num_lst.pop(0)
    if(len(num_lst)==1):
        break
    p2 = num_lst.pop(0)
    num_lst.append(p2)

print(num_lst[0])