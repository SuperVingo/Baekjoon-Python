a = int(input())

if(a == 1):
    print('1')
else:
    a -= 1
    cnt = 2
    while(True):
        a -= 6*(cnt - 1)
        if(a <= 0):
            print(cnt)
            break
        else:
            cnt += 1