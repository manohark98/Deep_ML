def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    m = len(a)
    n = len(a[0])



    b = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
   
            b[i][j] = a[j][i]
 
    return b