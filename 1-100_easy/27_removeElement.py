# 26ms
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums) - 1
        # nums = []
        if j == -1:
            return 0
        if j == 0:
            # nums = [val]
            if nums[0] == val:
                return 0
            # nums = [not val]
            return 1
        for i in range(j):
            if nums[i] == val:
                while nums[j] == val and j > i:
                    j -= 1
                # nums[j] != val, swap nums[i] and nums[j]
                nums[i] = nums[j]
                nums[j] = val
            # print("nums[{}]:{} nums[{}]:{} {}".format(i,nums[i], j, nums[j], nums))
        # do the exchanges
        if nums[j] == val:
            return j 
        # no exchange
        return len(nums)

nums = []

print(Solution().removeElement(nums, 4))
print(nums)