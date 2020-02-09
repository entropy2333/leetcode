class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def factorial(n):
            res = []
            res.append(1)
            for i in range(1, n+1):
                res.append(res[i-1]*i)
            return res
        fact = factorial(m + n - 2)
        return fact[m + n - 2] // (fact[m - 1] * fact[n - 1])

# 动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]