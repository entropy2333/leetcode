class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        flag = [[False] * n for _ in matrix]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(m * n):
            res.append(matrix[r][c])
            flag[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < m and 0 <= cc < n and not flag[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
            print("r: {} c:{} cr: {} cc: {} di: {} flag: {}".format(r, c, cr, cc, di, flag))
        return res

l = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
t = s.spiralOrder(l)