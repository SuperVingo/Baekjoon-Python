import math

def isPrime(n: int):
    if(n == 1):
        return False
    elif(n == 2):
        return True

    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

num = int(input())
orgin = num
lst = []
i = 2
if(isPrime(num)):
    print(num)
else:
    while(True):
        if(i > orgin // 2 + 2):
            break
        if(num % i == 0):
            lst.append(i)    
            num = num // i
        else:
            i += 1
        if(num == 1):
            break
    for i in lst:
        print(i)