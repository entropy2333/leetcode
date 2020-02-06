class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if nums[low] < nums[high]:
                if target <= nums[mid] and target >= nums[low]:
                    high = mid
                else:
                    low = mid
            else:
                if target <= nums[mid] and target >= nums[low]:
                    low = mid
                else:
                    high = mid
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        else:
            return -1

        