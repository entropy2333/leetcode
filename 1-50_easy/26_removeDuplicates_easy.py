# tld n^2
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 0
#         while i < len(nums):
#             j = i + 1
#             while j < len(nums):
#                 # print("i:{} j:{} nums:{} len:{}".format(i, j, nums, len(nums)))
#                 if nums[i] == nums[j] and i != j:
#                     nums.pop(j)
#                     j -= 1
#                 j += 1
#             i += 1
#         return len(nums)

# nums = [1, 1, 2, 3, 4]
# print(Solution().removeDuplicates(nums))
# print(nums)

# 72ms
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            print("i:{} j:{} nums:{} len:{}".format(i, j, nums, len(nums)))
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1 

nums = [1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5]
print(Solution().removeDuplicates(nums))
print(nums)