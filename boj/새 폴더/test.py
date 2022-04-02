import sys
import math
a = sys.maxsize
for i in range(100):
    a *= 492
for i in range(100):
    a /= 492

print(math.isclose(a,sys.maxsize))