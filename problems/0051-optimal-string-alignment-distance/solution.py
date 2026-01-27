def OSA(source: str, target: str) -> int:
	# Your code here
	n = len(source)
	m = len(target)
	
	# matrix: rows - source chars, cols - target chars
	d = [[0] * (m + 1) for _ in range(n + 1)]

	# edge initializing
	for i in range(n + 1):
		d[i][0] = i # cost of removing all chars from source
	for j in range(m + 1):
		d[0][j] = j # cost of inserting all chars to target
	
	# filling matrix
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			cost = 0 if source[i-1] == target[j-1] else 1

			d[i][j] = min(
				d[i-1][j] + 1,     # delete
				d[i][j-1] + 1, 	   # insert
				d[i-1][j-1] + cost # substitute
			)

			if i > 1 and j > 1 and source[i-1] == target[j-2] and source [i-2] == target[j-1]:
				d[i][j] = min(d[i][j], d[i-2][j-2] + 1)
	return d[n][m]