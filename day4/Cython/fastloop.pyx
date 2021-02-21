from math import exp
import numpy as np
from scipy.interpolate import Rbf

# Naive python implementation of a Radial Basis Function (RBF) approximation scheme
def rbf_network_cython(float[:,:] X, float[:] beta, int theta):
    cdef int N, D, i, j
    cdef float r

    N = X.shape[0]
    D = X.shape[1]
    
    cdef double[:] Y = np.zeros(N)
 #   cdef float[:] beta = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y


# Testing the performance of Cython
#t0 = time.time()
#rbf_network_cython(X, beta, theta)
#print("Cython: ", time.time() - t0)











        
