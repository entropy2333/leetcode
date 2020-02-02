class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            l = [0, 1, 2]
            for i in range(3, n+1):
                l.append(l[i-1] + l[i-2])
            return l[n]
    
print(Solution().climbStairs(5))