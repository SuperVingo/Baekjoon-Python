a = int(input())
t = 1
while(True):
    if(a - t > 0):
        a -= t
        t += 1
    else:
        t += 1
        break
if(t % 2 == 0):
    print(str(t-a) + "/" + str(a))
else:
    print(str(a) + "/" + str(t-a))