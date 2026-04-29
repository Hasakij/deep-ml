import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	x = np.array(x, dtype=float)
	n = len(x)
	f_x = np.array(f(x.tolist()), dtype=float)
	m = len(f_x)
	jacobian = np.zeros((m, n))

	for j in range(n):
		x_peturbed = x.copy()
		x_peturbed[j] += h
		f_peturbed = np.array(f(x_peturbed.tolist()), dtype=float)
		jacobian[:, j] = (f_peturbed - f_x) / h
	return jacobian.tolist()