cnt = 0
for i in range(6):
    line = input()
    if(line == 'W'):
        cnt += 1
if(cnt == 0):
    print(-1)
elif(cnt < 3):
    print(3)
elif(cnt < 5):
    print(2)
else:
    print(1)