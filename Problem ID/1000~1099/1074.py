import sys

N, r, c = map(int, sys.stdin.readline().strip().split())

def recur(x, y, l, s):
    if l <= 1:
        if x == c and y == r:
            return s
        elif (x+1) == c and y == r:
            return s + 1
        elif x == c and (y+1) == r:
            return s + 2
        elif ((x+1) == c) and ((y+1) == r):
            return s + 3

    l_x = x+(2 ** (l-1))
    l_y = y+(2 ** (l-1))
    if c < l_x and r < l_y:
        return recur(x, y, l-1, s)
    elif c >= l_x and r < l_y:
        return recur(x+2**(l-1), y, l-1, s + (4**(l-1)))
    elif c < l_x and r >= l_y:
        return recur(x, y+2**(l-1), l-1, s + (4**(l-1)) * 2)
    elif c >= l_x and r >= l_y:
        return recur(x+2**(l-1), y+2**(l-1), l-1, s + (4**(l-1)) * 3)

print(recur(0, 0, N, 0))