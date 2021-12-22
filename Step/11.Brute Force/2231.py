n = int(input())
found = False

def getSum(n:int):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum
    
for i in range(1, n):
    if(n == i + getSum(i)):
        found = True
        print(i)
        break

if(not found):
    print(0)