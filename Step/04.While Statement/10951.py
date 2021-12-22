while(True):
    try:
        user_input = input().split()
        a = int(user_input[0])
        b = int(user_input[1])
        print(a+b)
    except EOFError:
        break