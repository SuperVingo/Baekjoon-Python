x = []
y = []
for _ in range(3):
    line = input().split()
    x.append(int(line[0]))
    y.append(int(line[1]))

posx = posy = 0
if(x[0] == x[1]):
    posx = x[2]
elif(x[1] == x[2]):
    posx = x[0]
else:
    posx = x[1]

if(y[0] == y[1]):
    posy = y[2]
elif(y[1] == y[2]):
    posy = y[0]
else:
    posy = y[1]

print(posx, posy)