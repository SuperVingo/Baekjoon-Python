line = input().split()
a1 = int(line[0])
p1 = int(line[1])
line = input().split()
a2 = int(line[0])
p2 = int(line[1])

a = a1 + p2
b = p1 + a2
if(a > b):
    print('Persepolis')
elif(a < b):
    print('Esteghlal')
else:
    if(p1 > p2):
        print('Esteghlal')
    elif(p2 > p1):
        print('Persepolis')
    else:
        print('Penalty')