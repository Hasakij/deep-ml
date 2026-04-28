import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # val at point x
    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)
    
    # derivative values
    g_deriv_coeffs = [coeff * (len(g_coeffs) - 1 - i) for i, coeff in enumerate(g_coeffs[:-1])]
    h_deriv_coeffs = [coeff * (len(h_coeffs) - 1 - i) for i, coeff in enumerate(h_coeffs[:-1])]
    
    # derivative values at point x
    g_prime_x = np.polyval(g_deriv_coeffs, x) if g_deriv_coeffs else 0
    h_prime_x = np.polyval(h_deriv_coeffs, x) if h_deriv_coeffs else 0
    return (g_prime_x * h_x - g_x * h_prime_x) / (h_x ** 2)


