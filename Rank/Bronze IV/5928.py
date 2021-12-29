line = input().split()
d = int(line[0])
h = int(line[1])
m = int(line[2])
s = (d*1440 + h*60 + m) - (11*1440 + 11*60 + 11)
if(s < 0):
    print(-1)
else:
    print(s)