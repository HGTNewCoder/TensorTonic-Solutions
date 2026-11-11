import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.array(matrix)
    
    if (norm_type == 'l1'):
        ans = np.divide(matrix, np.sum(np.abs(matrix), axis = axis, keepdims=True))
        ans = np.where(np.isnan(ans), 0, ans)
        return ans
    elif (norm_type == 'l2'):
        ans = np.divide(matrix, np.sqrt(np.pow(matrix, 2).sum(axis = axis, keepdims=True)))
        ans = np.where(np.isnan(ans), 0, ans)
        return ans
    elif (norm_type == 'max'):
        ans = np.divide(matrix, np.max(matrix, axis = axis, keepdims=True))
        ans = np.where(np.isnan(ans), 0, ans)
        return ans

    