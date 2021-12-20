line = input().strip()
cnt = 0
for i in line:
    if(i == ' '):
        cnt = cnt + 1
if(len(line) == 0):
    print(0)
else:
    print(cnt + 1)