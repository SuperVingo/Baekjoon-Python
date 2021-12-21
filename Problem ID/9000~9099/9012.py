import sys


n = int(input())
for _ in range(n):
    stack = []
    success = True
    braket = sys.stdin.readline().strip()
    for i in braket:
        if(i == "("):
            stack.append(1)
        elif(i == ")"):
            if(len(stack) == 0):
                success = False
                break
            else:
                stack.pop()
    if(len(stack) == 0 and success == True):
        print("YES")
    else:
        print("NO")