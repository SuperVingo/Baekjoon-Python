n = int(input())
if(n == 1):
    print(1)
elif(n % 2 == 1):
    print(0)
else:
    while n != 0:
        if(n == 1):
            break
        elif(n % 2 == 1):
            print(0)
            exit(0)
        n = n // 2
    print(1)