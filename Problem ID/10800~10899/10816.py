n = int(input())
n_l = list(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split()))

n_dict = {}
for i in n_l:
    if i in n_dict.keys():
        n_dict[i] = n_dict[i] + 1
    else:
        n_dict[i] = 1 

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
    if i in n_dict.keys():
        print(n_dict[i], end=' ')
    else:
        print("0 ", end='')