# import time

# start = time.time()

# lst = [i for i in range(100000000)]

# for i in range(100000000):
#     lst[i] *= 100000000

# print("time1 : ", time.time() - start)

# start = time.time()

# lst = [i for i in range(100000000)]

# lst = list(map(lambda x: x*100000000,lst))

# print("time2 : ", time.time() - start)

lst = [1,2,3,4,5]
lst[2:4] = [10,11]
print(lst)
print(' ')
print(" ")

print(' '==None)
print(" "==None)