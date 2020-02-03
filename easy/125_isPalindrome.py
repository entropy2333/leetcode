class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def f(s):
            return s and s.isalnum()
        s = list(filter(f, s.lower()))
        return s == s[::-1]
