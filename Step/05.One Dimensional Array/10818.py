lst = []
num = int(input())
line = input().split()
for i in range(num):
    lst.append(int(line[i]))
print(min(lst), max(lst))