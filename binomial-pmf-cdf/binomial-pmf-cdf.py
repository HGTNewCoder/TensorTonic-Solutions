import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    f = lambda i: math.comb(n, i)*p**i * (1-p)**(n-i)
    pmf = float(f(k))
    cdf = float(sum([f(i) for i in range(k+1)]))
    return {'pmf': pmf, 'cdf': cdf}