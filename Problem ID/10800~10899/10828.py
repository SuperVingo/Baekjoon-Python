import sys

stack = []

n = int(input())
for _ in range(n):
    line = sys.stdin.readline().strip().split()
    if(line[0] == 'push'):
        stack.append(line[1])
    elif(line[0] == 'pop'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif(line[0] == 'size'):
        print(len(stack))
    elif(line[0] == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(line[0] == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack)-1])
