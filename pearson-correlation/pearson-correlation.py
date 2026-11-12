import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    
    mean = X.mean(axis = 0, keepdims=True)
    stdev = X.std(axis = 0, keepdims=True)

    Y = (X - mean) / np.sqrt(((X - mean)**2).sum(axis = 0, keepdims=True))

    return Y.T@Y