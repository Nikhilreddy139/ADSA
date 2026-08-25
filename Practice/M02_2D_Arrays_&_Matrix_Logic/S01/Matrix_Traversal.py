#1572.Problem: Matrix Diagonal Sum
from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
    n = len(mat)
    total_sum = 0
    for i in range(n):
        total_sum += mat[i][i]           
        if i != n - 1 - i:
            total_sum += mat[i][n - 1 - i]
    return total_sum
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))