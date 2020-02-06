class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)    
        pre = 0
        cur = 0
        for i in range(n):
            tmp = cur
            cur = max(pre + nums[i], cur)
            pre = tmp
        return cur