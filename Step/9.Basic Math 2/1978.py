import math

def isPrime(n: int):
    if(n == 1):
        return False
    elif(n == 2):
        return True

    for i in range(2, (n // 2 + 2)):
        if(n % i == 0):
            return False
    return True

n = int(input())
line = input().split()
cnt = 0
for i in line:
    num = int(i)
    if(isPrime(num)):
        cnt += 1
print(cnt)