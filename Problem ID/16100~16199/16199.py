line = input().split()
y1 = int(line[0])
m1 = int(line[1])
d1 = int(line[2])
line = input().split()
y2 = int(line[0])
m2 = int(line[1])
d2 = int(line[2])

if(y1 == y2):
    print(0)
else:
    if(m1 == m2):
        if(d1 <= d2):
            print(y2 - y1)
        else:
            print(y2 - y1 - 1)
    elif(m1 < m2):
        print(y2 - y1)
    else:
        print(y2 - y1 - 1)

print(y2 - y1 + 1)
print(y2 - y1)