import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    m = len(A)
    n = len(A[0])

    ans = []
    for i in range(n):
        temp_list = []
        for j in range(m):
            temp_list.append(A[j][i])
        ans.append(temp_list)

    return np.array(ans)
