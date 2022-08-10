n = int(input())
n_l = list(map(int, input().split()))
n_l.sort()
m = int(input())
m_l = list(map(int, input().split()))

def search(l, t):
    first = 0
    last = len(l) - 1
    
    while first <= last:
        mid = (first + last) // 2
        if l[mid] == t:
            return True
        elif l[mid] > t:
            last = mid - 1
        else:
            first = mid + 1
    return False

for i in m_l:
    if search(n_l, i):
        print("1 ", end='')
    else:
        print("0 ", end='')