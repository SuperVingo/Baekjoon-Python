line = input().split()
y = int(line[0])
x = int(line[1])
if(x == y):
    print(x/2)
    exit(0)
lst = []
if(y * 3 >= x): # ->
    lst.append(x/3)
else:
    lst.append(y)
if(x * 3 > y): # I
    lst.append(y/3)
else:
    lst.append(x)
if(y > x):
    lst.append(x/2)
else:
    lst.append(y/2)
print(max(lst))