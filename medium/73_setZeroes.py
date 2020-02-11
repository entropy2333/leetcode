class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag_line = False
        flag_row = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if (matrix[i][0] == 0):
                flag_row = True
                break
        for i in range(n):
            if (matrix[0][i]==0):
                flag_line = True
                break
        for i in range(1, m):
            for j in range(1,n):
                if (matrix[i][j] == 0):
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0            
        if (flag_row):
            for i in range(m):
                matrix[i][0] = 0
        if (flag_line):
            for i in range(n):
                matrix[0][i] = 0

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,0,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    print('res: {}'.format(matrix))