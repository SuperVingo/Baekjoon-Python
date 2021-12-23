line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
if(a == b and b == c):
    print(2)
else:
    m = max(a, b, c)
    if((m**2)*2 == a**2 + b**2 + c**2):
        print(1)
    else:
        print(0)