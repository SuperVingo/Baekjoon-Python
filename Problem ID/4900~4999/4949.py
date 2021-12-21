import sys

while(True):
    stack = []
    success = True
    braket = input()
    if(len(braket) == 1 and braket[0] == '.'):
        break
    for i in braket:
        if(i == "("):
            stack.append(1)
        elif(i == "["):
            stack.append(2)
        elif(i == ")"):
            if(len(stack) == 0):
                success = False
                break
            else:
                if(stack.pop() != 1):
                    success = False
                    break
        elif(i == "]"):
            if(len(stack) == 0):
                success = False
                break
            else:
                if(stack.pop() != 2):
                    success = False
                    break
    if(len(stack) == 0 and success == True):
        print("yes")
    else:
        print("no")