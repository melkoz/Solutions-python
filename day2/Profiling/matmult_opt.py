#!/usr/bin/env python
# Program to multiply two matrices using nested loops
import random
import numpy as np
n = 250

@profile
def x_gen(N):
    # NxN matrix
    X = np.random.randint(0,100,(N,N))
    return X

@profile
def y_gen(N):
    # Nx(N+1) matrix
    Y = np.random.randint(0,100,(N,N+1))
    return Y

@profile
def result_gen(N):
    # result is Nx(N+1)
    result = np.zeros((N,N+1))
    return result

@profile
def multipl(X,Y,result):

    result=  np.matmul(X,Y)
    return result 

@profile
def printing(result):
    for r in result:
        print(r)

x = x_gen(n)
y = y_gen(n)
res = result_gen(n)

result_final = multipl(x, y, res)
printing(result_final)
