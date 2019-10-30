# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if needle == '':
#             return 0
#         l = len(needle)
#         for i in range(len(haystack) - l + 1):
#             if haystack[i] == needle[0]:
#                 if haystack[i: i+l] == needle:
#                     return i
#         return (-1)

# haystack = 'arnwiadnaw'
# needle = 'a'
# print(Solution().strStr(haystack, needle))

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)