import numpy as np
from typing import List, Tuple

def fit_bradley_terry(comparisons: List[Tuple[int, int]], n_items: int, 
                      learning_rate: float = 0.5, n_iterations: int = 100) -> np.ndarray:
    """
    Fit Bradley-Terry model parameters using maximum likelihood estimation.
    
    Args:
        comparisons: List of (winner_idx, loser_idx) tuples
        n_items: Total number of items to rank
        learning_rate: Step size for gradient ascent
        n_iterations: Number of optimization iterations
    
    Returns:
        np.ndarray: Estimated strength parameters of shape (n_items,)
    """
    # Your code here
    beta = np.zeros(n_items)
    def sigmoid(x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    for _ in range(n_iterations):
        gradient = np.zeros(n_items)
        for w, l in comparisons:
            diff = beta[w] - beta[l]
            prob = sigmoid(diff)
            error = 1.0 - prob
            gradient[w] += error
           