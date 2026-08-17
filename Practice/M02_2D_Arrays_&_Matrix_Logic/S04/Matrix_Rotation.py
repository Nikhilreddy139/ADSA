#48.Problem:Rotate Image
'''from typing import List
def rotate(matrix: List[List[int]]) -> None:

    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)'''

#1886.Problem Statement: Determine whether matrix can be rotated to match target
from typing import List
def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for t in range(4):
            if mat==target:
                return True
            n = len(mat)
            for i in range(n):
                for j in range(i+1,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(n):
                mat[i].reverse()
        return False
mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
print(findRotation(mat,target))
