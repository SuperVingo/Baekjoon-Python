lst = [True] * 360000
lst[0] = False
lst[1] = False

for i in range(2, 701):
    for j in range(i*2, 360000, i):
        lst[j] = False

while(True):
    a = int(input())
    cnt = 0
    if(a == 0):
        break
    for i in range(a+1, a*2+1):
        if(lst[i]):
            cnt += 1
    print(cnt)