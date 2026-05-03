import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    x = np.array(x, dtype=float)
    analytical_grad = np.array(analytical_grad, dtype=float)
    numerical_grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += epsilon
        f_plus = f(x_plus)

        x_minus = x.copy()
        x_minus[i] -= epsilon
        f_minus = f(x_minus)

        numerical_grad[i] = (f_plus - f_minus) / (2 * epsilon)

    diff = numerical_grad - analytical_grad
    numerator = np.linalg.norm(diff)
    denominator = np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad)
    if denominator == 0:
        relative_error = 0.0
    else:
        relative_error = numerator / denominator
    return numerical_grad, relative_error