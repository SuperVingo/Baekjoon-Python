a = int(input())

a_5 = a//5
t = a % 5
if(t % 3 == 0):
    print(int(a_5 + t//3))
else:
    while(True):
        a_5 -= 1
        t += 5
        if(a_5 < 0):
            print('-1')
            break
        if(t % 3 == 0):
            print(int(a_5 + t//3))
            break