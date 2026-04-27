import numpy as np
import random

def smote(X_minority: np.ndarray, n_synthetic: int, k: int = 5, random_seed: int = 42) -> np.ndarray:
    """
    Generate synthetic samples using SMOTE algorithm.
    
    Args:
        X_minority: 2D array of minority class samples (n_samples, n_features)
        n_synthetic: Number of synthetic samples to generate
        k: Number of nearest neighbors to consider
        random_seed: Random seed for reproducibility
        
    Returns:
        2D array of synthetic samples (n_synthetic, n_features)
    """
    # Your code here
    
    np.random.seed(random_seed)
    n_samples, n_features = X_minority.shape
    if n_synthetic == 0:
        return np.empty((0, n_features))
    synthetic_samples = []
    
    # Use all available neighbors if minority samples are fewer than k+1
    actual_k = min(k, n_samples - 1)
    
    for i in range(n_synthetic):
        # Randomly select a sample from the minority class
        sample_idx = np.random.randint(0, n_samples)
        sample = X_minority[sample_idx]
        
        # Calculate Euclidean distances to all other samples
        diffs = X_minority - sample
        distances = np.sqrt(np.sum(diffs ** 2, axis=1))
        
        # Get k nearest neighbors (excluding the sample itself)
        # argsort by distance, then take the first actual_k elements (excluding index 0 which is the sample itself)
        nn_indices = np.argsort(distances)[1:actual_k + 1]
        
        # Randomly select one of the k nearest neighbors
        nn_idx = nn_indices[np.random.randint(0, actual_k)]
        neighbor = X_minority[nn_idx]
        
        # Generate synthetic sample along the line segment
        lambda_value = np.random.random()  # random value between 0 and 1
        synthetic_sample = sample + lambda_value * (neighbor - sample)
        synthetic_samples.append(synthetic_sample)
    
    return np.array(synthetic_samples)
