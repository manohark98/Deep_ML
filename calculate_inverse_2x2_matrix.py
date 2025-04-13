def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	
    m = len(matrix)
    n = len(matrix[0])
    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    matrix[0][0] , matrix[1][1] = matrix[1][1], matrix[0][0]
    matrix[0][1], matrix[1][0] =   -matrix[0][1] , -matrix[1][0]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = round((1/det)* matrix[i][j],1)
    
    return matrix