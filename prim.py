import numpy as np


def prim(C):
    A = np.array(C)
    A[A == 0] = 100
    l = A.shape[0]
    B = np.zeros(A.shape)

    loc = np.where(A == A.min())
    x = loc[0][0]
    y = loc[1][0]
    s = {x, y}
    B[x][y] = A[x][y]
    B[y][x] = A[x][y]
    A[x][y] = 100
    A[y][x] = 100
    for n in range(2,l):
        E = np.array([])
        for i in s:
            E = np.concatenate([E, A[i, :]])
        loc = np.where(A == E.min())
        x = loc[0][0]
        y = loc[1][0]
        s = s | {x, y}
        B[x][y] = A[x][y]
        B[y][x] = A[x][y]
        A[x][y] = 100
        A[y][x] = 100

    return B


a = np.array([[100, 5, 9, 100, 6],
              [5, 100, 3, 100, 100],
              [9, 3, 100, 100, 7],
              [100, 100, 10, 100, 5],
              [6, 10, 7, 5, 100]])

print(prim(a))
