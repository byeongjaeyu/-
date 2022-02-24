import sys

for line in sys.stdin:
    print(line)
    n,m = line.split()
    print(int(n)+int(m))
