import numpy as np
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	x = np.array(x, dtype=float)
	shifted_x = x - np.max(x)
	exp_x = np.exp(shifted_x)
	softmax = exp_x / np.sum(exp_x)
	jacobian = np.diag(softmax) - np.outer(softmax, softmax)
	return jacobian.tolist()
