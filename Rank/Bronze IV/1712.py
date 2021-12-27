import math

line = input().split()
A = int(line[0])
B = int(line[1])
C = int(line[2])

if(B >= C):
    print(-1)
else:
    print((A // (C - B))+1)