def pascalTriangle(till):
    matrix = []
    for i in range(till + 1):
        j = 0
        row = []
        while j <= i:
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(matrix[i - 1][j] + matrix[i - 1][j - 1])
            j += 1

        matrix.append(row)
    return matrix


"""
Complexity	    Value	    Explanation
Time	        O(till²)	Due to the nested loops (triangular number sum).
Space	        O(till²)	Due to the stored matrix (Pascal's Triangle).

for i = 0, j runs 1 times, for i = 1 , 2 times, for i = 2, 3 times, for i=3, 4 times and so on and so forth
its 1 + 2 + 3 ... + (till + 1) times ==> (till + 1) (till + 2) / 2 => O(till * till) complexity

Triangular Number Sum refers to the total number of elements in Pascal’s Triangle up to row till
"""
if __name__ == "__main__":
    result = pascalTriangle(10)
    for r in result:
        print(r)
