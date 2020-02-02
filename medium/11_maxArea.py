# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         area = 0
#         for i, a_i in enumerate(height):
#             for j, a_j in enumerate(height):
#                 area = max(area, (j-i)*min(a_i, a_j))
#         return area


class Solution(object):
    def maxArea(self, height):
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
