class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        binary_num1 = int('0b'+a, base=2)
        binary_num2 = int('0b'+b, base=2)
        return bin(binary_num1+binary_num2)[2:]

