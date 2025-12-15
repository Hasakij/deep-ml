import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    arr = np.array(vectors)
    cov_matrix = np.cov(arr, ddof=1)
	return cov_matrix