line = input().split()
x = int(line[0])
l = int(line[1])
r = int(line[2])

if(l <= x and x <= r):
    print(x)
else:
    if(abs(l-x) > abs(r-x)):
        print(r)
    else:
        print(l)