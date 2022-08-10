import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
if M != 0:
    D = sys.stdin.readline().strip().split()

i = N
while i >= 0:
    flag = False
    for j in str(i):
        if j in D:
            flag = True
    if not flag:
        break
    i -= 1
lower = i

i = N
if M != 9 or D[0] == '0':
    while True:
        flag = False
        for j in str(i):
            if j in D:
                flag = True
        if not flag:
            break
        i += 1
    upper = i
else:
    upper = 9999999999999

print(min(len(str(lower))+(N-lower), len(str(upper))+(upper-N), abs(100-N)))