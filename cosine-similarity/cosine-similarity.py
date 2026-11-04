import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    
    if a_norm == 0.0 or b_norm == 0.0:
        return 0.0
    else:
        cosine = (a@b) / (a_norm*b_norm)
        return float(cosine)
    