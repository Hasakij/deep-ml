import numpy as np

def rmsnorm(x: np.ndarray, g: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    """
    Apply RMSNorm to the input array.
    
    Parameters:
        x   : np.ndarray of shape (batch_size, features)
        g   : np.ndarray of shape (features,) - gain parameter
        eps : float - small constant for numerical stability
    
    Returns:
        np.ndarray of same shape as x
    """
    squared_vals = np.square(x)
    mean_squared_vals = np.mean(squared_vals, axis=-1, keepdims=True)
    rms = np.sqrt((mean_squared_vals + eps))
    rms_div = x / rms
    res = rms_div * g
    return res 