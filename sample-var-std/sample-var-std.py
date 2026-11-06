import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    variance = np.sum((x - mean)**2)/(x.shape[0] - 1)
    std = np.sqrt(variance)

    ans = {'variance': float(variance), 'standard_deviation': float(std)}
    return ans