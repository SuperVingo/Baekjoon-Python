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

min = int(input())
max = int(input())
lst = []
for i in range(min, max+1):
    if(isPrime(i)):
        lst.append(i)
if(len(lst) != 0):
    print(sum(lst))
    print(lst[0])
else:
    print(-1)