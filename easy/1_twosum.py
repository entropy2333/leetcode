# 穷举 4356ms 12.7MB
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     return [i, j]

# nums = [3, 2, 4]
# target = 6
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)

# Hash 52ms 13.4MB
# class Solution(object):
#     def twoSum(self, nums, target):
#         _dict = {}
#         # nums[i] = m
#         for i, m in enumerate(nums):
#             _dict[m] = i
        
#         for i, m in enumerate(nums):
#             # nums[j] = target - m 
#             # i.e. nums[i] + num[j] = target
#             j = _dict.get(target - m)
#             if j is not None and i != j:
#                 return [i, j]

# nums = [3, 2, 4]
# target = 6
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)

# Hash2 40ms 13.2MB
class Solution(object):
    def twoSum(self, nums, target):
        _dict = {}
        for i, m in enumerate(nums):
            # 动态添加，对每一个新添加的检查target
            if _dict.get(target - m) is not None:
                return [_dict.get(target - m), i]
            _dict[m] = i

nums = [3, 2, 4]
target = 6
solution = Solution()
result = solution.twoSum(nums, target)
print(result)