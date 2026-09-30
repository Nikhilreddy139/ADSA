from typing import List

def diagonalBoundarySum(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        for j in range(n):
            # Boundary elements
            boundary = i == 0 or i == n - 1 or j == 0 or j == n - 1

            # Diagonal elements
            diagonal = i == j or i + j == n - 1

            if boundary or diagonal:
                total += arr[i][j]

    return total


if __name__ == '__main__':
    n = int(input())

    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))

    print(diagonalBoundarySum(mat))