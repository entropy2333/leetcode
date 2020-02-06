class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        flag = False
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                flag = True
                if i == n-1:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    return nums
                else:
                    # sort = sorted(nums[i:])
                    index = nums.index(min(nums[i:]))
                    nums[i-1], nums[index] = nums[index]. nums[i-1]
                    nums[i:] = sorted(nums[i:])
        if not flag:
            return sorted(nums)