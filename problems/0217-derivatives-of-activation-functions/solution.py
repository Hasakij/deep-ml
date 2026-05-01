import math
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	sigmoid = 1 / (1 + math.exp(-x))
	deriv_sigmoid = sigmoid * (1 - sigmoid)
	tanh = (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
	deriv_tanh = 1 - tanh ** 2
	relu = max(0, x)
	if x > 0:
		deriv_relu = 1
	else:
		deriv_relu = 0
	return {
		'sigmoid': deriv_sigmoid,
		'tanh': deriv_tanh,
		'relu' : deriv_relu
	}