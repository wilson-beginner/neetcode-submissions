class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_size = len(matrix)
        col_size = len(matrix[0])
        row0 = False
        for i in range(row_size):
            for j in range(col_size):
                if matrix[i][j] == 0:
                    if i == 0: 
                        row0 = True
                        continue
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        #set zero row
        for i in range(1, row_size):
            if matrix[i][0] == 0:
                for j in range(1, col_size):
                    matrix[i][j] = 0

        #set zero col
        for j in range(0, col_size):
            if matrix[0][j] == 0:
                for i in range(1, row_size):
                    matrix[i][j] = 0
        #set row0
        if row0 == True:
            for j in range(col_size):
                matrix[0][j] = 0 