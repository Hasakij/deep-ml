import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	def square(x):
		return x**2
	def square_derivative(x):
		return 2 * x
	def sin_derivative(x):
		return np.cos(x)
	def exp_derivative(x):
		return np.exp(x)
	def log_derivative(x):
		return 1/x
	
	function_map = {
		'square': (np.square, lambda x: 2 * x),
		'sin': (np.sin, np.cos),
		'exp': (np.exp, np.exp),
		'log': (np.log, lambda x: 1/x)
	}

	values = [x]
	# from right to left, first the last function (the most inner)
	for func_name in reversed(functions):
		func, _ = function_map[func_name]
		current_value = values[-1]
		next_value = func(current_value)
		values.append(next_value)
	
	# values = [x, f1(x), f2(f1(x)), ..., fn(...f1(x))]

	derivative = 1.0
	for i, func_name in enumerate(reversed(functions)):
		_, derivative_func = function_map[func_name]
		point = values[i]
		derivative *= derivative_func(point)
	return derivative
