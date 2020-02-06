class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = bin(n)[2:]
        res = res.zfill(32)
        res = res[::-1]
        return int(res,base=2)
