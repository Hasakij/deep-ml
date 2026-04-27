import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	grad_array = np.array(gradient, dtype=float)
	if np.all(grad_array) == 0:
		return {
			'magnitude': 0.0,
			'direction': [0.0] * len(gradient),
			'descent_direction': [0.0] * len(gradient)
			} 
	magnitude = np.linalg.norm(grad_array)
	direction = (grad_array / magnitude).tolist()
	descent_direction = (-grad_array / magnitude).tolist()
	return {
		'magnitude': float(magnitude),
		'direction': direction,
		'descent_direction': descent_direction
		}