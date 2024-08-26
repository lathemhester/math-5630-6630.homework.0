# Author: Your Name / your_email
# Date: 2024-09-01
# Assignment Name: hw00

import numpy as np
import time 

# The following class defines 3 functions for each problem respectively.
# Please follow the instruction inside each function. 

def p1(m):
    """
    This function takes an integer m and returns the term a_m in the sequence defined by 
    a_0 = 0, a_1 = 1, a_2 = 1, and a_n = a_{n-1} + a_{n-2} + a_{n-3} for n >= 3.
    :param m: an integer
    :return: the m-th term in the sequence
    """
    if m < 0:
        return None
    elif m == 0:
        return 0
    elif m == 1 or m == 2:
        return 1
    else:
        arr = [0, 1, 1]
        for i in range(m - 2):  # Loop runs (m-2) times to get up to the m-th term
            nextNum = np.sum(arr)
            arr.append(nextNum)
            arr.pop(0)
        return np.sum(arr)

def p2(A):
    """
    This function takes a numpy matrix A of size n x n and returns the determinant of A.
    :param A: a numpy matrix of size n x n
    :return: the determinant of A
    """
    if A.shape[0] != A.shape[1]:
        return None
    else:
        pass # add your code here

def p3():
    """
    This function should have a run time about 1 second.
    :return: no returns
    """
    
    pass # add your code here
