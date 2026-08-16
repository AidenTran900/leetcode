class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range (n):
            for j in range(i+1, n):
                saved = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = saved
        
        for row in matrix:
            row.reverse()

        print(matrix)