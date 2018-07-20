import numpy as np
import scipy as scp

def dijkstra(C):
    A=np.array(C).astype(np.float32)
    A[A==0]=scp.inf
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

a = np.array([[0, 10, 0, 30, 100],
              [0, 0, 50, 0, 0],
              [0, 0, 0, 0, 10],
              [0, 0, 0, 0, 60],
              [0, 0, 0, 0, 0]])
a=a+a.T
print dijkstra(a)