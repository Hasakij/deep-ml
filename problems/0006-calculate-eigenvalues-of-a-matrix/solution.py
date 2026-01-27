import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	# tr(A) = a + d
	# det(A) = ad - bc
	a = matrix[0][0] 
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	trace = a + d
	determinant = a * d - b * c
	delta = trace**2 - 4 * determinant
	lambda1 = (trace + math.sqrt(delta)) / 2
	lambda2 = (trace - math.sqrt(delta)) / 2
	eigenvalues = [lambda1, lambda2]
	eigenvalues.sort(reverse=True)
	return eigenvalues