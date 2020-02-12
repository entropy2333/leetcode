class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head = head << 1
        return res

if __name__ == "__main__":
    s = Solution()
    n = [0, 1, 2, 3, 4]
    res = map(s.grayCode, n)
    print(list(res))