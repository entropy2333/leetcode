# 52ms 11.7MB
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i, m in enumerate(s):
            if i < (len(s) - 1) and d[m] < d[s[i+1]]:
                num -= d[m]
            else:
                num += d[m]
        return num

print(Solution().romanToInt('CIX'))