A = int(input())
B = int(input())
C = int(input())

total = A * B * C

lst = [0] * 10
for i in str(total):
    lst[int(i)] = lst[int(i)] + 1
    
for i in lst:
    print(i)