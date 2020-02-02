class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        s = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(13):
            if num > 0:
                digits[i] = num // s[i]
                num = num - digits[i]*s[i]
        t = ''
        for i in range(13):
            for j in range(digits[i]):
                t += d[i]

        return t


print(Solution().intToRoman(2345))     
# l = [0, 1, 2, 3, 4]
