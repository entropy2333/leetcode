from functools import reduce
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        def convertToDec(x, y):
            return 26*x + y
        def convert(ch):
            return ord(ch) - 64
        s = list(map(convert, s))
        s = reduce(convertToDec, s)
        return s