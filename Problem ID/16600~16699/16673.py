line = input().split()
c = int(line[0])
k = int(line[1])
p = int(line[2])
cnt = 0
for i in range(1, c+1):
    cnt += k*i + p*(i**2)
print(cnt)