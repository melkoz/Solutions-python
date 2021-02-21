#!/usr/bin/env python
import random

n = 250


#@profile
def x_gen(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    return X

#@profile
def y_gen(N):
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    return Y

#@profile
def result_gen(N):
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    return result


#@profile
def iterating(X,Y,result):
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

#@profile
def printing(result):
    for r in result:
        print(r)

x = x_gen(n)
y = y_gen(n)
res = result_gen(n)

result_final = iterating(x, y, res)
printing(result_final)
