#74.Problem: Search a 2D Matrix
'''from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = searchMatrix(matrix, target)
if result:
    print(f"{target} is found in the matrix.")
else:
    print(f"{target} is not found in the matrix.")'''

#240.Problem: Search a 2D Matrix II
def searchMatrixII(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]] 
target = 5
result = searchMatrixII(matrix, target)
if result:
    print(f"{target} is found in the matrix.")
else:
    print(f"{target} is not found in the matrix.")

#378.Problem: Kth Smallest Element in a Sorted Matrix
from typing import List
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    import heapq
    min_heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heapq.heappush(min_heap, matrix[i][j])
    for _ in range(k - 1):
        heapq.heappop(min_heap)
    return heapq.heappop(min_heap)
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
result = kthSmallest(matrix, k)
print(f"The {k}th smallest element in the matrix is: {result}")
matrix = [[-5]]
k = 1
result = kthSmallest(matrix, k)
print(f"The {k}th smallest element in the matrix is: {result}")