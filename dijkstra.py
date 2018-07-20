import numpy as np


def dijkstra(C):
    A=np.array(C)
    m = A.shape[0]
    r = range(0, m)
    while True:
        for i in r:
            finished = True
            for j in r:
                for k in r:
                    if i != j and A[i, k] + A[k, j] < A[i, j]:
                        A[i, j] = A[i, k] + A[k, j]
                        A[j, i] = A[i, k] + A[k, j]
                        finished = False
            if finished:
                return A

a = np.array([[100, 5, 9, 100, 100],
              [5, 100, 3, 100, 100],
              [9, 3, 100, 100, 7],
              [100, 100, 100, 100, 5],
              [100, 100, 7, 5, 100]])

print dijkstra(a)