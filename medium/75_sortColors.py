class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        cur = 0
        while cur <= r:
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
                cur += 1
            elif nums[cur] == 2:
                nums[r], nums[cur] = nums[cur], nums[r]
                r -= 1
            else:
                cur += 1