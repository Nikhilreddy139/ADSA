def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Start from every column in the first row
    for start_col in range(cols):
        values = []
        i, j = 0, start_col

        while i < rows and j < cols:
            values.append(mat[i][j])
            i += 1
            j += 1

        values.sort()

        i, j = 0, start_col
        k = 0

        while i < rows and j < cols:
            mat[i][j] = values[k]
            i += 1
            j += 1
            k += 1

    # Start from every row in the first column
    for start_row in range(1, rows):
        values = []
        i, j = start_row, 0

        while i < rows and j < cols:
            values.append(mat[i][j])
            i += 1
            j += 1

        values.sort()

        i, j = start_row, 0
        k = 0

        while i < rows and j < cols:
            mat[i][j] = values[k]
            i += 1
            j += 1
            k += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())

    mat = []
    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))