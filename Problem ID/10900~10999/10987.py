line = input()
cnt = 0
vow = ['a', 'e', 'i', 'o', 'u']
for i in line:
    if(i in vow):
        cnt += 1
print(cnt)