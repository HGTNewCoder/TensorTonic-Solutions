import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    N = len(v)
    ans = []
    for i in range(N):
        temp = []
        for j in range(N):
            if i == j:
                temp.append(v[i])
            else:
                temp.append(0)
        ans.append(temp)

    return np.array(ans)