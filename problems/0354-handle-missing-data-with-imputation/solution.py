import numpy as np
from collections import Counter
def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    res = data.copy()
    
    for i in range(res.shape[1]): # iterating over columns
        col = res[:, i]
        mask = np.isnan(col) # mask of missing values in this column
        
        # skip if all values or all missing values
        if not mask.any() or mask.all():
            continue
            
        non_nan_values = col[~mask] # only existing values
        
        if strategy == 'mean':
            fill_value = np.mean(non_nan_values)
        elif strategy == 'median':
            fill_value = np.median(no