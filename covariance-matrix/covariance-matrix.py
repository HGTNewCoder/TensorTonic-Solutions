import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X)
    mean = np.mean(X, axis=0, keepdims=True)
    Xc = X - mean
    covariance_matrix = (Xc.T @ Xc) / (X.shape[0] - 1)
    return covariance_matrix