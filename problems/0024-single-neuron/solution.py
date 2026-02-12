import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	def sigmoid(z):
		return 1 / (1 + np.exp(-z))
	# Your code here
	features = np.array(features)
	labels = np.array(labels)
	weights = np.array(weights)
	bias = np.array(bias)
	weighted_sum = (features @ weights + bias)
	probabilities = sigmoid(weighted_sum)
	mse = np.mean((probabilities - labels)**2)
	return np.round(probabilities, 4).tolist(), round(float(mse), 4)