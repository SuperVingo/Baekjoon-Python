line = input().split()
ax = int(line[0])
ay = int(line[1])
az = int(line[2])
print(int((ax+1)*(ay+1) / (az+1) - 1))