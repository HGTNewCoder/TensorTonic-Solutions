import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    N = len(A)
    sum = 0
    for i in range (N):
        sum+= A[i][i]
    return float(sum)