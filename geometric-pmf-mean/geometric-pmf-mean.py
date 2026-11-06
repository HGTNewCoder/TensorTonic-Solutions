import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    # Write code here
    f = lambda i: (1-p)**(i-1) * p
    pmf = np.array([f(i) for i in k])
    mean = float(1/p)
    return {'pmf': pmf, 'mean': mean}