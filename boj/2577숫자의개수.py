a = 1
for i in range(3):
    a *= int(input())

a = str(a)
print(a)
for i in range(10):
    print(a.count(str(i)))