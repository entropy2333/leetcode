# 60ms 11.6MB
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         return (str(x)[::-1] == str(x))

# 40ms 11.8MB
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        if s[0] == '-':
            return False
        return (s[::-1] == s)
print(Solution().isPalindrome(-100))