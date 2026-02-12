def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	# Your code here
	if z < 0:
		res = alpha * z
	else:
		res = z
	return res
