#!/usr/bin/env python
"""
A collection of simple math operations
"""

def simple_add(a,b):
    ''' Performs a sum of 'a' and 'b' variables.
    
    Parameters
    ----------
    a, b : integer or float.
    
    Returns
    -------
    a + b : integer or float.
    
    Examples
    --------
    >>> simple_add(2,2)                                                                                                                                       
    4
    >>> simple_add(2,1.5)                                                                                                                                     
    3.5
    >>> simple_add(2.9,1.5)                                                                                                                                   
    4.4
    '''
    return a+b

def simple_sub(a,b):
    ''' Substracts 'b' from 'a'.
    
    Parameters
    ----------
    a, b : integer or float.
    
    Returns
    -------
    a - b : integer or float.
    
    Examples
    --------
    >>> simple_sub(2,2)       
    0
    >>> simple_sub(2,1.5)   
    0.5
    >>> simple_sub(2.9,1.5) 
    1.4
    '''
    return a-b

def simple_mult(a,b):
    ''' Performs a multiplication of 'a' and 'b' variables.
    
    Parameters
    ----------
    a, b : integer or float.
    
    Returns
    -------
    a * b : integer or float.
    
    Examples
    --------
    >>> simple_mult(2,2)     
    4
    >>> simple_mult(2,1.5)  
    3.0
    '''
    return a*b

def simple_div(a,b):
    ''' Performs a division of 'a' by 'b'.

    Parameters
    ----------
    a, b : float.

    Returns
    -------
    a/b : float.

    Examples
    --------
    >>> simple_mult(2,2)    
    1.0
    >>> simple_mult(3,1.5) 
    2.0
    '''
    return a/b

def poly_first(x, a0, a1):
    ''' First degree polynomial where a0 is the y-intercept and a1 is the slope.
    
    Parameters
    ----------
    x, a0, a1 : integer or float.
    
    Returns
    -------
    a0 + a1*x : integer or float.
    
    Examples
    --------
    >>> poly_first(2,2,2)  
     6
    >>> poly_first(2,2,2.5)
     7.0
    '''
    
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    ''' Second degree polynomial.
    
    Parameters
    ----------
    x, a0, a1, a2 : integer or float.
    
    Returns
    -------
    a0 + a1*x + a2*(x**2) : integer or float.
    
    Examples
    --------
    >>> poly_second(2,2,2,2)                                                                                                                                  
     14
    >>> poly_second(2,2,2,2.5)                                                                                                                                
     16.0
    '''    
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
