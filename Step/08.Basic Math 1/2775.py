case = int(input())

for i in range(case):
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    k = int(input())
    n = int(input())

    for j in range(0, k):
        for l in range(0, 14):
            if(j % 2 == 0):
                lst2[l] = sum(lst1[:l+1])
            else:
                lst1[l] = sum(lst2[:l+1])
    if(j % 2 == 0):
        print(lst2[n-1])
    else:
        print(lst1[n-1])