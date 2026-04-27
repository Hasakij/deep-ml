def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    deriv = c * n * x**(n - 1)
    #deriv_val = deriv * x
    return deriv