num = int(input())
for z in range(num):
    line = input().split()
    lst = []

    for i in range(int(line[0])):
        lst.append(int(line[i+1]))
    
    avg = sum(lst) / len(lst)

    cnt = 0
    for i in lst:
        if(i > avg):
            cnt = cnt + 1
    
    print("%.3f%%" % (cnt / len(lst) * 100))