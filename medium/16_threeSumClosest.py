class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if not nums or n < 3:
            return
        nums.sort()

        res = float('inf') 

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                cur_sum = nums[i] + nums[L] + nums[R]

                if cur_sum == target:
                    return cur_sum
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum < target:
                    L += 1
                if cur_sum > target:
                    R -= 1
        return res