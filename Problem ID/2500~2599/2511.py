a = list(map(int, input().split()))
b = list(map(int, input().split()))
asc = 0
bsc = 0
last = 0 # 1 -> a
for (a1, b1) in zip(a, b):
    if(a1 > b1):
        last = 1
        asc += 3
    elif(a1 < b1):
        last = -1
        bsc += 3
    else:
        asc += 1
        bsc += 1
print(asc, bsc)
if(asc > bsc):
    print('A')
elif(asc < bsc):
    print('B')
else:
    if(last == 1):
        print('A')
    elif(last == -1):
        print('B')
    else:
        print('D')