class Solution:
    def numTrees(self, n: int) -> int:
        res = [1, 1]
        for i in range(2, n + 1):
            tmp = 0
            l = len(res)
            for j in range(l):
                tmp += res[j] * res[l - j]
            res.append(tmp)
        return res[n]