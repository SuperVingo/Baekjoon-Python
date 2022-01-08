import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    a = int(sys.stdin.readline().strip())
    s = 0
    for j in range(2, a+1):
        t = a
        while t >= j:
            if(t%j==0):
                s += 1
                t = t // j
            else:
                break
    print(s)