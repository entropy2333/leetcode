class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        d = {}
        l = len(nums)
        result = []
        nums.sort()
        for i in range(l):
            if nums[i] > 0:
                break
            for j in range(i+1, l):
                if (nums[i]+nums[j]) not in d:
                    d[nums[i]+nums[j]] = []
                d[nums[i]+nums[j]].append([i, j])

        for i, x in enumerate(nums):
            if (-x) in d:
                for num in d[-x]:
                    if i not in num:
                        temp = sorted([nums[i], nums[num[0]], nums[num[1]]])
                        if temp not in result:
                            result.append(temp)
        return result