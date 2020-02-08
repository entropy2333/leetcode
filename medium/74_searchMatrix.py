class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1 

        while low < high:
            mid = (low + high) // 2
            i, j = divmod(mid, n)
            element = matrix[i][j]
            if target == element:
                return True
            elif element > target:
                high = mid
            else:
                low = mid+1
        return False