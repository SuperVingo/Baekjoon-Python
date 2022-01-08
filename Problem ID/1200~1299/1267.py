y = 0
m = 0
n = int(input())
line = input().split()
for i in line:
    y += ((int(i) // 30) + 1) * 10
    m += ((int(i) // 60) + 1) * 15

if(y > m):
    print('M ' + str(m))
elif(y < m):
    print('Y ' + str(y))
else:
    print('Y M ' + str(m))