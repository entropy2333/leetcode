class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                nums.pop(i)