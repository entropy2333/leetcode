class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        def findLow(nums):
            low = 0
            high = len(nums)
            while low < high:
                mid = (low + high) // 2
                if (target <= nums[mid]):
                    high = mid
                else:
                    low = mid + 1
            return low
        def findHigh(nums):
            low = 0
            high = len(nums)
            while low < high:
                mid = (low + high) // 2
                if (target < nums[mid]):
                    high = mid
                else:
                    low = mid + 1
            return low
        low = findLow(nums)
        if low == len(nums) or nums[low] != target:
            return [-1, -1]
        high = findHigh(nums)
        return [low, high-1]