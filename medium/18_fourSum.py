class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()

        result = []

        for i in range(n):
            if i < n-3 and nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                return result 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp = self.threeSum(nums[i+1:], target-nums[i])
            if not tmp:
                continue
            result.extend([[nums[i]] + x for x in tmp])
        return result

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if not nums or n < 3:
            return []

        result = []

        for i in range(n):
            if i < n-2 and nums[i] + nums[i+1] + nums[i+2] > target:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == target:
                    result.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > target:
                    R -= 1
                else:
                    L += 1
        return result
