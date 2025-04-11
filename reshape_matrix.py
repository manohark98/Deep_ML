import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    m = len(a)
    n = len(a[0])
    if m*n != new_shape[0]*new_shape[1]:
        return []
    reshaped_matrix = [[0 for _ in range(m)] for _ in range(n)]
	
    k = 0
    l = 0
    for i in range(n):
        for j in range(m):
            if l == n:
                l = 0
                k+=1
            reshaped_matrix[i][j] = a[k][l]
            l+=1
    return reshaped_matrix