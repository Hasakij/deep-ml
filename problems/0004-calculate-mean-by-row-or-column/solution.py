import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    arr = np.array(matrix)
    if mode == 'row':
        means = arr.mean(axis=1)
    elif mode == 'column':
        means = arr.mean(axis=0)
    else:
        raise ValueError("Mode must be either 'row' or 'column'")
	return means