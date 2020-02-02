class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        if l == 0:
            digits.insert(0, 1)
            return digits
        else:
            if digits[-1] == 9:
                digits[-1] = 0
                digits[:l-1] = self.plusOne(digits[:l-1])
                return digits
            else:
                digits[-1] += 1
                return digits
