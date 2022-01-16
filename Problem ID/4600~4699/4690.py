for i in range(5, 101):
    a = i

    for j in range(1, 101):
        for k in range(1, 101):
            for l in range(1, 101):
                if(a ** 3 == j ** 3 + k ** 3 + l ** 3):
                    print('Cube = %d, Triple = (%d,%d,%d)' % (a, j, k, l))