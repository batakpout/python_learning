from typing import List

##matrix can be of any dimension
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Create a new transposed matrix with dimensions cols x rows
    transposed = [[0] * rows for _ in range(cols)] # todo find out how this works

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

"""
Time Complexity: O(rows * cols), where rows is the number of rows and cols is the number of columns in the input matrix.

Space Complexity: O(rows * cols), for storing the transposed matrix.
"""