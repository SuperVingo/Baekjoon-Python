line = input().split()
a = int(line[0])
b = int(line[1])
aa = abs(a)
ab = abs(b)
if(a == 0):
    print(0)
    print(0)
elif(a > 0):
    if(b > 0):
        print(aa//ab)
        print(aa%ab)
    else:
        print(-(aa//ab))
        print(aa%ab)
else:
    if(b > 0):
        print(-((aa//ab) + 1))
        print(ab - abs(aa%ab))
    else:
        print(((aa//ab) + 1))
        print(ab - abs(aa%ab))