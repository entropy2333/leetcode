class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        max_index = 0
        for i in range(n):
            # print(max_index)
            if max_index >= i and i + nums[i] > max_index:
                max_index = i + nums[i]
        return max_index >= n-1
    
if __name__ == "__main__":
    solution = Solution()
    l = [0]
    res = solution.canJump(l)
    print(res)