lst = [0, 1]

def f (a: int):
    for i in range(2, a+1):
        lst.append(lst[i-1] + lst[i-2])
    print(lst[a])
f(int(input()))