# 44ms
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for num in nums:
#             if num == target:
#                 return nums.index(num)
#             if num > target:
#                 return nums.index(num)
#         return len(nums)

# print(Solution().searchInsert([1,3,5,6],7))

# 二分查找
class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r) //2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        if target>nums[l]:
            return l + 1
        else:
            return l