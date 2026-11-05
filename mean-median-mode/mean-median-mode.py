from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = sorted(x)

    cnt = {}
    for i in x:
        if str(i) in cnt.keys():
            cnt[str(i)] += 1
        else:
            cnt[str(i)] = 1

    mode = list(cnt)[0]
    for i in cnt:
        if cnt[i] > cnt[mode]:
            mode = i
        
    
    x = np.array(x)
    mean = np.mean(x)
    median = np.median(x)
        

    # return {'mean': float(mean), 'median': float(median), 'mode': float(mode)}
    return {'mean': float(mean), 'median': float(median), 'mode': float(mode)}