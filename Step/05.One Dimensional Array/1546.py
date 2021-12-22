lst = []
num = int(input())
line = input().split()
for i in range(num):
    lst.append(int(line[i]))

m = max(lst)
for i in range(num):
    lst[i] = lst[i] / m * 100

print(sum(lst) / num)
