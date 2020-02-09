class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0] * n for i in range(n)]
        flag = [[False] * n for i in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(n * n):
            res[r][c] = i+1
            flag[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < m and 0 <= cc < n and not flag[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
            print("r: {} c:{} cr: {} cc: {} di: {} flag: {}".format(r, c, cr, cc, di, flag))
        return res