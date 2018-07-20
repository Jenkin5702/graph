import numpy as np


def kruskal(C):
    A = np.array(C)
    l = A.shape[0]
    B = np.zeros(A.shape)
    for n in range(0, l - 1):
        loc = np.where(A == A.min())
        x = loc[0][0]
        y = loc[1][0]
        print([x, y])
        cir = False
        for i in range(0, l):
            if B[x][i] * B[i][y] != 0:
                cir = True
                break
        if not cir:
            B[x][y] = A[x][y]
            B[y][x] = A[x][y]
        A[x][y] = 100
        A[y][x] = 100
    return B


a = np.array([[100, 5, 9, 100, 100],
              [5, 100, 3, 100, 100],
              [9, 3, 100, 100, 7],
              [100, 100, 100, 100, 5],
              [100, 100, 7, 5, 100]])

print(kruskal(a))