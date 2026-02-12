import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	mse_list = []
	def sigmoid(z):
		return 1 / (1 + np.exp(-z))
	w = initial_weights.copy()
	b = initial_bias
	for _ in range(epochs):
		z = np.dot(features, w) + b
		probs = sigmoid(z)
		mse = np.mean((probs - labels)**2)
		mse_list.append(round(float(mse), 4))
		n = len(labels)
		error = probs - labels
		sig_der = probs * (1 - probs)
		grad_base = (2 / n) * error * sig_der
		dw = np.dot(features.T, grad_base)
		db = np.sum(grad_base)
		w -= dw * learning_rate
		b -= db * learning_rate
	return np.round(w, 4).tolist(), np.round(float(b) ,4), mse_list