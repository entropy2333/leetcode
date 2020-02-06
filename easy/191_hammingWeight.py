class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        cnt = 0
        for ch in s:
            cnt += int(ch)
        return cnt