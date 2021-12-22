num = int(input())
new_num = num
cnt = 1
while(True):
    back = (new_num // 10 + new_num % 10) % 10
    new_num = (new_num % 10) * 10 + back
    if(num == new_num):
        break
    cnt = cnt+1
print(cnt)