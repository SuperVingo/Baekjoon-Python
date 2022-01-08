line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])
line = input().split()
p = int(line[0]) - 1
m = int(line[1]) - 1
n = int(line[2]) - 1

ap = p % (a+b) + 1
am = m % (a+b) + 1
an = n % (a+b) + 1
bp = p % (c+d) + 1
bm = m % (c+d) + 1
bn = n % (c+d) + 1
if(ap <= a and bp <= c):
    print(2)
elif(ap <= a or bp <= c):
    print(1)
else:
    print(0)
if(am <= a and bm <= c):
    print(2)
elif(am <= a or bm <= c):
    print(1)
else:
    print(0)
if(an <= a and bn <= c):
    print(2)
elif(an <= a or bn <= c):
    print(1)
else:
    print(0)