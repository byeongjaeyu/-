from collections import Counter

n = int(input())
num_lst = [0]*n
for i in range(len(num_lst)):
    num_lst[i] = int(input())

num_lst.sort()
p = 0
for num in num_lst:
    p += num

print(round(p/n))

print(num_lst[n // 2])


nums_s = Counter(num_lst).most_common()
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

print(num_lst[-1]-num_lst[0])
