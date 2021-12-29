line = input().split()
a1 = int(line[0])
a2 = int(line[2])
a3 = int(line[4])
line = input().split()
b1 = int(line[0])
b2 = int(line[2])
b3 = int(line[4])
n = (b1*3600 + b2*60 + b3) - (a1*3600 + a2*60 + a3)
if(n < 0):
    print(n + 24*3600)
else:
    print(n)
