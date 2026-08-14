#867.Problem Statement: Transpose of a Matrix
from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))
