import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    f = np.array(f_coeffs, dtype=float)
    g = np.array(g_coeffs, dtype=float)
    product = np.convolve(f, g)
    derivative = np.array([i * product[i] for i in range(1, len(product))])
    if len(derivative) == 0:
        return [0.0]
    derivative = np.round(derivative, 4)
    result = derivative.tolist()
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result