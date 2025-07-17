def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    out = []
    for row in a:
        sum_ = 0
        if len(row) != len(b):
            return -1
        for row_element, vector_element  in zip(row, b):
            sum_ += row_element * vector_element
        out.append(sum_)
    return out
