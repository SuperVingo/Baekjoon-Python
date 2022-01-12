while True:
    try:
        print(input())
    except KeyboardInterrupt:
        break
    except EOFError:
        break