#1351.Problem:Count Negative Numbers in a Sorted Matrix
'''from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    for row in grid:
        for num in row:
            if num < 0:
                count += 1
    return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print("Count of negative numbers in the matrix:", countNegatives(grid))
(OR)
from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] < 0:
                count += 1
    return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))'''

#832.Problem: Flipping an Image
from typing import List
def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for row in image:
        row.reverse()
        for i in range(len(row)):
            row[i] = 1 - row[i]
    return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))