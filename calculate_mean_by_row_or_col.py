def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	m = len(matrix)
	n = len(matrix[0])

	res = []

	if mode == "column":
		for j in range(n):
			temp = 0
			for i in range(m):
				temp+= matrix[i][j]
			res.append(temp//m)
	else:
		for i in range(m):
			res.append(sum(matrix[i])//n)
	
	return res