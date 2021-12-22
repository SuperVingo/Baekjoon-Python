while(True):
    user_input = input().split()
    a = int(user_input[0])
    b = int(user_input[1])
    if(a == 0 and b == 0):
        break
    print(a+b)