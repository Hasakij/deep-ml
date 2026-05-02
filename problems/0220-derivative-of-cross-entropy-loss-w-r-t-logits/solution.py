import numpy as np
def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Your code here
	logits = np.array(logits, dtype=float)
	shifted_logits = logits - np.max(logits)
	exp_z = np.exp(shifted_logits)
	softmax = exp_z / np.sum(exp_z)
	n = len(logits)
	y = np.zeros(n)
	y[target] = 1.0
	gradient = softmax - y
	return gradient.tolist()