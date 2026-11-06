import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    
    pmf = lambda k: p**k * (1-p)**(1-k)
    mean = p
    var = p*(1-p)
    return {'pmf': np.array([pmf(i) for i in x]), 'mean': float(mean), 'variance': float(p*(1-p))}