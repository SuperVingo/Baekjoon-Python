import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
if M != 0:
    D = sys.stdin.readline().strip().split()

    # Find Upper
    i = N-1

    while i >= 0:
        flag = False
        for j in str(i):
            if j in D:
                flag = True
                break
        
        if flag:
            i -= 1
        else:
            break

    if i == -1:
        lower = -999999999999
    else:
        lower = i

    i = N
    flag = False
    while i <= 1100000:
        flag = False
        for j in str(i):
            if j in D:
                flag = True
                break
        
        if flag:
            i += 1
        else:
            break

    upper = i

    print(min(len(str(lower))+(N-lower), len(str(upper))+(upper-N), abs(100-N)))
else:
    print(min(abs(100-N), len(str(N))))