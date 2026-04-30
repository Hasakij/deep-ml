from typing import Callable
import numpy as np
def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Hessian matrix of function f at the given point using finite differences.
	
	Args:
		f: A scalar function that takes a list of floats and returns a float
		point: The point at which to compute the Hessian (list of coordinates)
		h: Step size for finite differences (default: 1e-5)
		
	Returns:
		The Hessian matrix as a list of lists (n x n where n = len(point))
	"""
	# Your code here
	n = len(point)
	hessian = np.zeros((n,n))
	point = np.array(point, dtype=float)

	f_x = f(point.tolist())
	for i in range(n):
		x_plus = point.copy()
		x_plus[i] += h
		f_plus = f(x_plus.tolist())

		x_minus = point.copy()
		x_minus[i] -= h
		f_minus = f(x_minus.tolist())

		hessian[i, i] = (f_plus - 2 * f_x + f_minus) / h**2

		for j in range(i+1, n):
			x_pp = point.copy()
			x_pp[i] += h
			x_pp[j] += h
			f_pp = f(x_pp.tolist())

			x_pm = point.copy()
			x_pm[i] += h
			x_pm[j] -= h
			f_pm = f(x_pm.tolist())

			x_mp = point.copy()
			x_mp[i] -= h
			x_mp[j] += h
			f_mp = f(x_mp.tolist())

			x_mm = point.copy()
			x_mm[i] -= h
			x_mm[j] -= h
			f_mm = f(x_mm.tolist())

			mixed = (f_pp - f_pm - f_mp + f_mm) / (4 * h**2)

			hessian[i, j] = mixed
			hessian[j, i] = mixed
	return hessian