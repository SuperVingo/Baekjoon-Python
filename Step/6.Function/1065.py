def isHan(n: int):
    if(n < 100):
        return True
    elif(n < 1000):
        if(((n // 100) - ((n % 100) // 10)) == (((n % 100) // 10) - (n % 10))):
            return True
    return False

cnt = 0
n = int(input())
for i in range(1, n+1):
    if(isHan(i)):
        cnt =  cnt + 1

print(cnt)