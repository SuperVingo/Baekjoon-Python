lst = [0] * 42
for i in range(10):
    num = int(input()) % 42
    lst[num] = lst[num] + 1
    
cnt = 0
for i in lst:
    if(i != 0):
        cnt = cnt + 1

print(cnt)