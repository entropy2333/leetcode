class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        #print(dp)
        for i in range(m):
            for j in range(n):
                # print(dp)
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    l = [[0,0,0],[0,1,0],[0,0,0]]
    res = s.uniquePathsWithObstacles(l)
    print(res)