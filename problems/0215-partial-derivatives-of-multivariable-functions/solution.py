import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	if func_name=='poly2d':
		deriv_x = 2 * point[0] * point[1] + point[1]**2
		deriv_y = point[0] ** 2 + 2 * point[0] * point[1]
		return (deriv_x, deriv_y)
	elif func_name=='exp_sum':
		deriv_x = np.exp(point[0] + point[1])
		deriv_y = np.exp(point[0] + point[1])
		return (deriv_x, deriv_y)
	elif func_name=='product_sin':
		deriv_x = np.sin(point[1])
		deriv_y = point[0] * np.cos(point[1])
		return (deriv_x, deriv_y)
	elif func_name=='poly3d':
		deriv_x = 2 * point[0] * point[1]
		deriv_y = point[0] ** 2 + point[2] ** 2
		deriv_z = 2 * point[1] * point[2]
		return (deriv_x, deriv_y, deriv_z)
	elif func_name=='squared_error':
		deriv_x = 2 * (point[0] - point[1])
		deriv_y = -2 * (point[0] - point[1])
		return (deriv_x, deriv_y)
